#!/usr/bin/env python3
"""Rebuild every Phlo AI-training diagram, then verify the whole repo is Style B.

    python3 build_all.py

Runs every videos/**/build*.py in its own subprocess (so each gets a clean
module state and its own random seed), then runs the STYLE-B GUARD over every
.excalidraw in the repo. The guard HARD-FAILS on the Style A signature - frames,
or typed (non-hand) fonts - so the editorial purple style can never silently
creep back in. Off-palette colours are reported as warnings.

Exit code is non-zero if any build errors or the guard hard-fails (CI-friendly).
"""
import glob
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from excalidraw_kit import PALETTE  # noqa: E402

HAND_FONTS = {1, 5}  # 5 = Excalifont (current), 1 = legacy hand font (llm_explainer)


def build():
    scripts = sorted(glob.glob(os.path.join(ROOT, "videos", "**", "build*.py"), recursive=True))
    ok = True
    for s in scripts:
        rel = os.path.relpath(s, ROOT)
        r = subprocess.run([sys.executable, s], capture_output=True, text=True)
        if r.returncode == 0:
            print(f"  built  {rel}  ->  {r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ''}")
        else:
            ok = False
            print(f"  ERROR  {rel}\n{r.stderr.strip()}")
    return ok


def guard():
    ok = True
    for f in sorted(glob.glob(os.path.join(ROOT, "**", "*.excalidraw"), recursive=True)):
        rel = os.path.relpath(f, ROOT)
        els = json.load(open(f)).get("elements", [])
        hard, warn = [], []
        frames = sum(1 for e in els if e.get("type") == "frame")
        if frames:
            hard.append(f"{frames} frame(s)")
        bad_font = sorted({e.get("fontFamily") for e in els
                           if e.get("type") == "text" and e.get("fontFamily") not in HAND_FONTS})
        if bad_font:
            hard.append(f"typed fonts {bad_font}")
        off = sorted({c for e in els for k in ("strokeColor", "backgroundColor")
                      for c in [e.get(k)] if c is not None and c not in PALETTE})
        if off:
            warn.append(f"off-palette {off[:4]}")
        if hard:
            ok = False
            print(f"  STYLE A  {rel}: " + "; ".join(hard))
        elif warn:
            print(f"  warn     {rel}: " + "; ".join(warn))
        else:
            print(f"  ok       {rel}")
    return ok


if __name__ == "__main__":
    print("=== BUILD ===")
    b = build()
    print("\n=== STYLE-B GUARD ===")
    g = guard()
    print(f"\nBUILD {'OK' if b else 'FAILED'}  |  GUARD {'PASS' if g else 'FAIL (Style A detected)'}")
    sys.exit(0 if (b and g) else 1)
