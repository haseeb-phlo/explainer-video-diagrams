#!/usr/bin/env python3
"""
Compile llm_explainer.excalidraw + llm_explainer.excalimate.json into an
Excalimate checkpoint that the Excalimate UI can load directly.

Input schema (llm_explainer.excalimate.json):
  { version, title, TOTAL_DURATION_MS, fps, background, defaults,
    sections: [{ id, name, startMs, endMs, elements: [
        { elementId, enter:{type,atMs,durationMs,...},
          exit:{type,atMs,durationMs}, hold:{fromMs,toMs},
          emphasis:[{type,atMs,durationMs}] } ] }],
    cameraHints: [{ atMs, focusElementId, zoom }] }

Output schema (Excalimate checkpoint):
  { scene:{elements,files}, timeline:{id,name,duration,fps,tracks},
    clipStart, clipEnd, cameraFrame }

Animation translation:
  fade enter    -> opacity 0 -> 1
  draw enter    -> drawProgress 0 -> 1 (arrows/lines) | opacity 0 -> 1 (others)
  slide enter   -> translateX/Y offset -> 0, with opacity 0 -> 1
  fade exit     -> opacity 1 -> 0
  pulse         -> scaleX/Y 1 -> 1.1 -> 1 with center-origin translate compensation
  shake         -> translateX oscillation
  cameraHints   -> __camera_frame__ translateX/Y + scaleX/Y keyframes
"""

import json
import secrets
import string
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_DIR = ROOT / "videos" / "ai-foundations" / "1-what-is-ai"
PLAN_PATH = VIDEO_DIR / "llm_explainer.excalimate.json"
DIAG_PATH = VIDEO_DIR / "llm_explainer.excalidraw"
OUT_PATH = VIDEO_DIR / "llm_explainer.checkpoint.json"

SLIDE_OFFSET = 150
PULSE_SCALE = 1.1
CAMERA_WIDTH = 1200
CAMERA_ASPECT = "16:9"

_NID_ALPHABET = string.ascii_letters + string.digits + "-_"

# Excalidraw uses fractional indices for Z-order. The "integer part" prefix
# encodes digit count: a=1 digit, b=2 digits, c=3 digits, … using base-62
# (0-9, A-Z, a-z). So a0..az is 0..61, then b00..bzz is 62..3905, etc.
_FI_DIGITS = string.digits + string.ascii_uppercase + string.ascii_lowercase  # 62 chars


def fractional_index(n: int) -> str:
    """Return the nth canonical fractional index in ascending order."""
    if n < 0:
        raise ValueError("negative index not supported")
    if n < 62:
        return "a" + _FI_DIGITS[n]
    if n < 62 + 62 * 62:
        m = n - 62
        return "b" + _FI_DIGITS[m // 62] + _FI_DIGITS[m % 62]
    raise ValueError("more than 3906 elements not supported")


def nid(n: int = 21) -> str:
    return "".join(secrets.choice(_NID_ALPHABET) for _ in range(n))


class TrackBuilder:
    def __init__(self):
        self._by_key: dict[tuple[str, str], list[tuple[float, float, str]]] = {}

    def add(self, target_id: str, prop: str, time: float, value: float, easing: str = "linear"):
        self._by_key.setdefault((target_id, prop), []).append((time, value, easing))

    def to_tracks(self) -> list[dict]:
        out = []
        for (tid, prop), kfs in self._by_key.items():
            # Dedupe by time: later writes win (so e.g. a pulse anchor at t=at
            # overrides a stale value from an earlier exit-fade).
            by_time: dict[float, tuple[float, str]] = {}
            for t, v, e in sorted(kfs, key=lambda x: x[0]):
                by_time[t] = (v, e)
            kfs_final = sorted(by_time.items())
            out.append({
                "id": nid(),
                "targetId": tid,
                "targetType": "group" if tid == "__camera_frame__" else "element",
                "property": prop,
                "keyframes": [
                    {"id": nid(), "time": t, "value": v, "easing": e}
                    for t, (v, e) in kfs_final
                ],
                "enabled": True,
            })
        return out


def apply_enter(eid: str, etype: str, enter: dict, tb: TrackBuilder):
    typ = enter["type"]
    at = enter["atMs"]
    dur = enter["durationMs"]
    end = at + dur

    if typ == "fade":
        tb.add(eid, "opacity", 0, 0)
        tb.add(eid, "opacity", at, 0)
        tb.add(eid, "opacity", end, 1, "easeOutCubic")
    elif typ == "draw":
        if etype in ("arrow", "line"):
            tb.add(eid, "opacity", 0, 1)
            tb.add(eid, "drawProgress", 0, 0)
            tb.add(eid, "drawProgress", at, 0)
            tb.add(eid, "drawProgress", end, 1, "easeOutCubic")
        else:
            tb.add(eid, "opacity", 0, 0)
            tb.add(eid, "opacity", at, 0)
            tb.add(eid, "opacity", end, 1, "easeOutCubic")
    elif typ == "slide":
        tb.add(eid, "opacity", 0, 0)
        tb.add(eid, "opacity", at, 0)
        tb.add(eid, "opacity", end, 1, "easeOutCubic")
        direction = enter.get("from", "bottom")
        dx = dy = 0
        if direction == "top":
            dy = -SLIDE_OFFSET
        elif direction == "bottom":
            dy = SLIDE_OFFSET
        elif direction == "left":
            dx = -SLIDE_OFFSET
        elif direction == "right":
            dx = SLIDE_OFFSET
        if dx:
            tb.add(eid, "translateX", at, dx)
            tb.add(eid, "translateX", end, 0, "easeOutCubic")
        if dy:
            tb.add(eid, "translateY", at, dy)
            tb.add(eid, "translateY", end, 0, "easeOutCubic")
    else:
        tb.add(eid, "opacity", 0, 0)
        tb.add(eid, "opacity", at, 0)
        tb.add(eid, "opacity", end, 1, "easeOutCubic")


def apply_exit(eid: str, ex: dict, tb: TrackBuilder):
    typ = ex["type"]
    at = ex["atMs"]
    end = at + ex["durationMs"]
    if typ == "fade":
        tb.add(eid, "opacity", at, 1)
        tb.add(eid, "opacity", end, 0, "easeInCubic")


def apply_emphasis(eid: str, el: dict, em: dict, tb: TrackBuilder):
    typ = em["type"]
    at = em["atMs"]
    dur = em["durationMs"]
    mid = at + dur / 2
    end = at + dur

    if typ == "pulse":
        w = el.get("width", 0) or 0
        h = el.get("height", 0) or 0
        cx = -w * (PULSE_SCALE - 1) / 2
        cy = -h * (PULSE_SCALE - 1) / 2
        tb.add(eid, "scaleX", at, 1, "easeOutQuad")
        tb.add(eid, "scaleY", at, 1, "easeOutQuad")
        tb.add(eid, "scaleX", mid, PULSE_SCALE, "easeOutQuad")
        tb.add(eid, "scaleY", mid, PULSE_SCALE, "easeOutQuad")
        tb.add(eid, "scaleX", end, 1, "easeOutQuad")
        tb.add(eid, "scaleY", end, 1, "easeOutQuad")
        if cx:
            tb.add(eid, "translateX", at, 0, "easeOutQuad")
            tb.add(eid, "translateX", mid, cx, "easeOutQuad")
            tb.add(eid, "translateX", end, 0, "easeOutQuad")
        if cy:
            tb.add(eid, "translateY", at, 0, "easeOutQuad")
            tb.add(eid, "translateY", mid, cy, "easeOutQuad")
            tb.add(eid, "translateY", end, 0, "easeOutQuad")
    elif typ == "shake":
        steps = [
            (at, 0),
            (at + dur * 0.15, -8),
            (at + dur * 0.35, 8),
            (at + dur * 0.55, -4),
            (at + dur * 0.75, 4),
            (end, 0),
        ]
        for t, v in steps:
            tb.add(eid, "translateX", t, v, "easeInOutQuad")


def element_center(el: dict) -> tuple[float, float]:
    return (el["x"] + el.get("width", 0) / 2, el["y"] + el.get("height", 0) / 2)


def normalize_element(el: dict, idx: int) -> dict:
    """Mirror Excalimate's elementNormalizer: fill in fields the renderer needs.

    Most importantly `index` (fractional Z-order, "a0".."a203") — without it the
    Excalidraw renderer silently fails to draw and the Excalimate UI shows an
    empty 16:9 frame with a broken play button.
    """
    out = {
        "angle": 0,
        "strokeColor": "#1e1e1e",
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "groupIds": [],
        "frameId": None,
        "index": fractional_index(idx),
        "roundness": None,
        "boundElements": None,
        "updated": el.get("updated", 0),
        "link": None,
        "locked": False,
        "isDeleted": False,
    }
    if el.get("type") == "text":
        out.update({
            "fontSize": 20,
            "fontFamily": 5,
            "textAlign": "left",
            "verticalAlign": "top",
            "lineHeight": 1.25,
            "baseline": 0,
            "containerId": None,
            "originalText": el.get("text", ""),
            "autoResize": True,
        })
    if el.get("type") in ("arrow", "line"):
        w = el.get("width", 100)
        h = el.get("height", 0)
        out.update({
            "points": el.get("points", [[0, 0], [w, h]]),
            "startBinding": None,
            "endBinding": None,
            "startArrowhead": None,
            "endArrowhead": "arrow" if el.get("type") == "arrow" else None,
            "lastCommittedPoint": None,
        })
    out.update(el)
    if el.get("type") == "text":
        out["fontFamily"] = 5
        if not el.get("containerId"):
            out["autoResize"] = True
    out.setdefault("seed", 1)
    out.setdefault("version", 1)
    out.setdefault("versionNonce", 1)
    return out


def main():
    plan = json.loads(PLAN_PATH.read_text())
    diag = json.loads(DIAG_PATH.read_text())

    elements = [normalize_element(e, i) for i, e in enumerate(diag["elements"])]
    elements_by_id = {e["id"]: e for e in elements}

    tb = TrackBuilder()
    missing: list[str] = []

    for sec in plan["sections"]:
        for el_plan in sec["elements"]:
            eid = el_plan["elementId"]
            el = elements_by_id.get(eid)
            if el is None:
                missing.append(eid)
                continue
            etype = el.get("type", "")
            if "enter" in el_plan:
                apply_enter(eid, etype, el_plan["enter"], tb)
            if "exit" in el_plan:
                apply_exit(eid, el_plan["exit"], tb)
            for em in el_plan.get("emphasis", []) or []:
                apply_emphasis(eid, el, em, tb)

    duration = max(s["endMs"] for s in plan["sections"])
    fps = plan.get("fps", 24)

    # Camera: anchor on first hint, then animate translate/scale at each subsequent hint.
    hints = plan.get("cameraHints", []) or []
    cam_x = cam_y = 0.0
    if hints:
        first = hints[0]
        ref = elements_by_id.get(first["focusElementId"])
        if ref is not None:
            cam_x, cam_y = element_center(ref)
        else:
            missing.append(first["focusElementId"])
        first_zoom = first.get("zoom", 1.0) or 1.0
        first_scale = 1.0 / first_zoom
        tb.add("__camera_frame__", "translateX", 0, 0)
        tb.add("__camera_frame__", "translateY", 0, 0)
        tb.add("__camera_frame__", "scaleX", 0, first_scale)
        tb.add("__camera_frame__", "scaleY", 0, first_scale)
        for hint in hints[1:]:
            ref = elements_by_id.get(hint["focusElementId"])
            if ref is None:
                missing.append(hint["focusElementId"])
                continue
            fx, fy = element_center(ref)
            tx = fx - cam_x
            ty = fy - cam_y
            zoom = hint.get("zoom", 1.0) or 1.0
            scale = 1.0 / zoom
            t = hint["atMs"]
            tb.add("__camera_frame__", "translateX", t, tx, "easeInOutCubic")
            tb.add("__camera_frame__", "translateY", t, ty, "easeInOutCubic")
            tb.add("__camera_frame__", "scaleX", t, scale, "easeInOutCubic")
            tb.add("__camera_frame__", "scaleY", t, scale, "easeInOutCubic")

    checkpoint = {
        "scene": {"elements": elements, "files": diag.get("files", {})},
        "timeline": {
            "id": nid(),
            "name": plan.get("title", "Timeline 1"),
            "duration": duration,
            "fps": fps,
            "tracks": tb.to_tracks(),
        },
        "clipStart": 0,
        "clipEnd": duration,
        "cameraFrame": {
            "aspectRatio": CAMERA_ASPECT,
            "width": CAMERA_WIDTH,
            "x": cam_x,
            "y": cam_y,
        },
    }

    OUT_PATH.write_text(json.dumps(checkpoint, indent=2))

    print(f"Wrote {OUT_PATH.relative_to(ROOT)}")
    print(f"  elements: {len(elements)}")
    print(f"  tracks:   {len(checkpoint['timeline']['tracks'])}")
    print(f"  duration: {duration} ms ({duration/1000:.1f}s)")
    print(f"  fps:      {fps}")
    print(f"  camera:   ({cam_x:.0f}, {cam_y:.0f}) {CAMERA_WIDTH}px {CAMERA_ASPECT}")
    if missing:
        print(f"  WARNING: {len(missing)} plan references not in diagram:", file=sys.stderr)
        for m in missing[:10]:
            print(f"    - {m}", file=sys.stderr)


if __name__ == "__main__":
    main()
