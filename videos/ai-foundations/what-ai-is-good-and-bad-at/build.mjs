// Phlo AI Training - Video 1.3 "What AI is good at, what it's bad at"
// Drives the live Excalimate MCP server (localhost:3001) over streamable HTTP.
//
// Commands:
//   node build.mjs scene1     push Scene 1 only (elements+kf+camera frame+clip), then verify
//   node build.mjs rest       add Scenes 2-7 elements+kf + camera pans + clip range
//   node build.mjs verify     framing checks at each scene hold time
//   node build.mjs finalize   save checkpoint + share link
//   node build.mjs dump <f>   write current scene to <f> as .excalidraw
import fs from "node:fs";

const URL = "http://localhost:3001/mcp";
const H = { "Content-Type": "application/json", Accept: "application/json, text/event-stream" };
function parseSSE(t) { let o = ""; for (const l of t.split(/\r?\n/)) if (l.startsWith("data:")) o += l.slice(5).trim(); try { return JSON.parse(o); } catch { return { raw: t }; } }
let SID = null, ID = 1;
async function rpc(method, params) {
  const headers = { ...H }; if (SID) headers["mcp-session-id"] = SID;
  const body = { jsonrpc: "2.0", id: ID++, method, ...(params !== undefined ? { params } : {}) };
  const res = await fetch(URL, { method: "POST", headers, body: JSON.stringify(body) });
  SID = res.headers.get("mcp-session-id") || SID;
  return parseSSE(await res.text());
}
async function notify(method) { const headers = { ...H }; if (SID) headers["mcp-session-id"] = SID; await fetch(URL, { method: "POST", headers, body: JSON.stringify({ jsonrpc: "2.0", method }) }); }
async function init() { await rpc("initialize", { protocolVersion: "2024-11-05", capabilities: {}, clientInfo: { name: "phlo-build", version: "1" } }); await notify("notifications/initialized"); }
async function call(name, args) {
  const r = await rpc("tools/call", { name, arguments: args });
  if (r.error) { console.error("TOOL ERROR", name, JSON.stringify(r.error)); process.exit(1); }
  const txt = r.result?.content?.map((c) => c.text).join("\n") ?? JSON.stringify(r.result);
  return txt;
}

// ---------- palette ----------
const INK = "#1e1e1e", GREY = "#868e96", GREEN = "#2f9e44", AMBER = "#f08c00", RED = "#e03131", BLUE = "#1971c2";
const TINT_G = "#ebfbee", TINT_A = "#fff9db", TINT_R = "#fff5f5", PAPER = "#f8f9fa", WHITE = "#ffffff";
const FF = 5; // Excalifont (hand-drawn)

// ---------- element helpers ----------
const E = [];           // elements accumulator
const K = [];           // keyframe accumulator
function push(...els) { E.push(...els); }
function rect(id, x, y, w, h, stroke = INK, bg = "transparent", extra = {}) {
  push({ id, type: "rectangle", x, y, width: w, height: h, strokeColor: stroke, backgroundColor: bg, fillStyle: "solid", strokeWidth: 2, roughness: 1.5, roundness: { type: 3 }, opacity: 100, ...extra }); return id;
}
function ellipse(id, x, y, w, h, stroke = INK, bg = "transparent", extra = {}) {
  push({ id, type: "ellipse", x, y, width: w, height: h, strokeColor: stroke, backgroundColor: bg, fillStyle: "solid", strokeWidth: 2, roughness: 1.5, opacity: 100, ...extra }); return id;
}
// centered free text box
function text(id, cx, cy, str, size = 28, color = INK, w = null, align = "center") {
  const width = w ?? Math.max(40, str.length * size * 0.58);
  const height = size * 1.25 * (str.split("\n").length);
  push({ id, type: "text", x: cx - width / 2, y: cy - height / 2, width, height, text: str, fontSize: size, fontFamily: FF, textAlign: align, verticalAlign: "middle", strokeColor: color, opacity: 100 });
  return id;
}
// left-anchored text (lists)
function textL(id, lx, cy, str, size = 26, color = INK, w = 700) {
  const height = size * 1.25 * (str.split("\n").length);
  push({ id, type: "text", x: lx, y: cy - height / 2, width: w, height, text: str, fontSize: size, fontFamily: FF, textAlign: "left", verticalAlign: "middle", strokeColor: color, opacity: 100 });
  return id;
}
function line(id, x, y, pts, stroke = INK, sw = 3, extra = {}) {
  let minx = 0, miny = 0, maxx = 0, maxy = 0; for (const [px, py] of pts) { minx = Math.min(minx, px); miny = Math.min(miny, py); maxx = Math.max(maxx, px); maxy = Math.max(maxy, py); }
  push({ id, type: "line", x, y, width: maxx - minx, height: maxy - miny, points: pts, strokeColor: stroke, strokeWidth: sw, roughness: 1.5, opacity: 100, ...extra }); return id;
}
function arrow(id, x, y, pts, stroke = INK, sw = 3, extra = {}) {
  let maxx = 0, maxy = 0; for (const [px, py] of pts) { maxx = Math.max(maxx, px); maxy = Math.max(maxy, py); }
  push({ id, type: "arrow", x, y, width: maxx, height: maxy, points: pts, strokeColor: stroke, strokeWidth: sw, roughness: 1.5, endArrowhead: "arrow", opacity: 100, ...extra }); return id;
}

// ---------- keyframe helpers (absolute ms) ----------
function appear(id, t, dur = 600, ease = "easeOut") {
  K.push({ targetId: id, property: "opacity", time: 0, value: 0 });
  K.push({ targetId: id, property: "opacity", time: t, value: 0 });
  K.push({ targetId: id, property: "opacity", time: t + dur, value: 1, easing: ease });
}
// drawProgress reveal for lines/arrows (opacity stays 1; nothing draws until t)
function draw(id, t, dur = 700, ease = "easeInOut") {
  K.push({ targetId: id, property: "drawProgress", time: 0, value: 0 });
  K.push({ targetId: id, property: "drawProgress", time: t, value: 0 });
  K.push({ targetId: id, property: "drawProgress", time: t + dur, value: 1, easing: ease });
}
function kf(id, prop, t, value, easing) { K.push({ targetId: id, property: prop, time: t, value, ...(easing ? { easing } : {}) }); }

// ---------- layout ----------
const GAP = 2400;                  // horizontal distance between scene centers
const CY = 470;                    // common vertical center
const CAM_W = 1700;                // camera width (16:9 -> h ~956)
const cx = (i) => 1000 + (i - 1) * GAP;   // scene i center x (1-indexed)
const START = { 1: 0, 2: 30000, 3: 120000, 4: 160000, 5: 200000, 6: 240000, 7: 270000 };
const CLIP_END = 300000;

// ============================================================
// SCENE 1 - Hook: confidence != accuracy  (~0:00-0:30)
// ============================================================
function scene1() {
  const C = cx(1), s = START[1];
  // big takeaway + underline at top
  const head = text("s1-take", C, 150, "Confidence ≠ accuracy.  Fluent ≠ correct.", 50, INK, 1500);
  const ul = line("s1-ul", C - 720, 195, [[0, 0], [1440, 0]], AMBER, 5);
  // intern doodle (left)
  const ihx = C - 560;
  rect("s1-head", ihx - 70, 300, 140, 110, INK, "#a5d8ff");      // robot head
  ellipse("s1-eye1", ihx - 38, 335, 26, 26, INK, WHITE);
  ellipse("s1-eye2", ihx + 12, 335, 26, 26, INK, WHITE);
  line("s1-mouth", ihx - 26, 385, [[0, 0], [52, 0]], INK, 3);
  line("s1-ant", ihx, 300, [[0, 0], [0, -34]], INK, 3);
  ellipse("s1-antb", ihx - 9, 248, 18, 18, INK, AMBER);
  rect("s1-body", ihx - 55, 430, 110, 90, INK, PAPER);
  text("s1-internlbl", ihx, 560, "Your AI intern", 28, INK, 360);
  // group robot parts so they fade together
  for (const id of ["s1-head", "s1-eye1", "s1-eye2", "s1-mouth", "s1-ant", "s1-antb", "s1-body", "s1-internlbl"]) {
    const elx = E.find((e) => e.id === id); elx.groupIds = ["s1-robot"];
  }
  // gauges (right) - Confidence (pinned MAX) & Accuracy (wobbling low)
  const g1x = C + 130, g2x = C + 520, gy = 400, R = 95;
  ellipse("s1-g1", g1x - R, gy - R, R * 2, R * 2, INK, WHITE);
  text("s1-g1max", g1x + 78, gy - 70, "MAX", 18, GREEN, 90);
  text("s1-g1low", g1x - 78, gy + 60, "low", 16, GREY, 70);
  // needle: vertical line, bbox-center near dial center (small tail) -> rotation reads as a dial
  line("s1-n1", g1x, gy - 80, [[0, 0], [0, 110]], RED, 4);
  text("s1-g1lbl", g1x, gy + R + 36, "Confidence", 28, INK, 280);
  ellipse("s1-g2", g2x - R, gy - R, R * 2, R * 2, INK, WHITE);
  text("s1-g2max", g2x + 78, gy - 70, "MAX", 18, GREEN, 90);
  text("s1-g2low", g2x - 78, gy + 60, "low", 16, GREY, 70);
  line("s1-n2", g2x, gy - 80, [[0, 0], [0, 110]], AMBER, 4);
  text("s1-g2lbl", g2x, gy + R + 36, "Accuracy", 28, INK, 240);
  // caption
  text("s1-cap", C, 700, "Brilliant, fast - and confidently wrong\nmore often than you'd think on niche questions.", 28, GREY, 1100);

  // ---- animation ----
  appear("s1-robot", s + 200, 700);
  // gauges fade in
  for (const id of ["s1-g1", "s1-g1max", "s1-g1low", "s1-g1lbl", "s1-g2", "s1-g2max", "s1-g2low", "s1-g2lbl"]) appear(id, s + 1200, 600);
  // confidence needle: low-left -> sweeps up and locks at MAX (right)
  appear("s1-n1", s + 1400, 300);
  kf("s1-n1", "rotation", s + 1700, -75);
  kf("s1-n1", "rotation", s + 3400, 78, "easeOutBack");
  kf("s1-n1", "rotation", s + 30000, 78);          // stays pinned
  // accuracy needle: jitters between low and mid
  appear("s1-n2", s + 1400, 300);
  const wob = [[-58, 2000], [-22, 3200], [-50, 4200], [-30, 5200], [-52, 6200], [-34, 7400], [-48, 9000], [-38, 11000], [-46, 14000], [-40, 30000]];
  for (const [v, dt] of wob) kf("s1-n2", "rotation", s + dt, v, "easeInOut");
  // caption + takeaway + underline
  appear("s1-cap", s + 4000, 700);
  appear("s1-take", s + 6500, 700);
  draw("s1-ul", s + 7400, 1100);
}

// ============================================================
// SCENE 2 - The map: three zones  (~0:30-2:00)
// ============================================================
function scene2() {
  const C = cx(2), s = START[2];
  text("s2-title", C, 90, "Three zones. Know which one you're in.", 44, INK, 1300);
  const laneW = 480, laneH = 640, top = 200, gap = 60;
  const totalW = laneW * 3 + gap * 2; const leftX = C - totalW / 2;
  const lanes = [
    { id: "g", x: leftX, stroke: GREEN, bg: TINT_G, head: "🟢  GREEN", sub: "Let it run - glance & ship",
      items: ["• first drafts of anything", "• summarising", "• restructuring messy notes", "• comparing options", "• brainstorming", "• writing & explaining code", "• translation", "• explaining things simply", "• generating examples"] },
    { id: "a", x: leftX + laneW + gap, stroke: AMBER, bg: TINT_A, head: "🟡  AMBER", sub: "Verify before it leaves",
      items: ["• specific facts & numbers", "• names, dates, recent events", "• customer-facing copy", "", "AI drafts it -", "you check every specific", "before it goes out."] },
    { id: "r", x: leftX + (laneW + gap) * 2, stroke: RED, bg: TINT_R, head: "🔴  RED", sub: "A qualified human must own it",
      items: ["• clinical decisions", "• dosing checks", "• regulatory commitments", "• apologies after a real failure", "", "anything a patient or", "regulator relies on."] },
  ];
  lanes.forEach((L, li) => {
    rect(`s2-${L.id}-box`, L.x, top, laneW, laneH, L.stroke, L.bg, { strokeWidth: 3 });
    text(`s2-${L.id}-head`, L.x + laneW / 2, top + 50, L.head, 34, L.stroke, laneW - 30);
    text(`s2-${L.id}-sub`, L.x + laneW / 2, top + 105, L.sub, 22, INK, laneW - 30);
    line(`s2-${L.id}-rule`, L.x + 30, top + 145, [[0, 0], [laneW - 60, 0]], L.stroke, 2);
    const items = [];
    L.items.forEach((it, idx) => {
      if (it === "") return;
      const isNote = !it.startsWith("•");
      const id = `s2-${L.id}-it${idx}`;
      textL(id, L.x + 34, top + 195 + idx * 48, it, isNote ? 21 : 24, isNote ? GREY : INK, laneW - 50);
      items.push(id);
    });
    // animation: lane box + header reveal, then stagger items
    const ls = s + li * 9000;        // green ~30-39s, amber ~39-48s, red ~48-57s (room to spare in the 30-120s window)
    appear(`s2-${L.id}-box`, ls + 200, 600);
    appear(`s2-${L.id}-head`, ls + 500, 500);
    appear(`s2-${L.id}-sub`, ls + 900, 500);
    draw(`s2-${L.id}-rule`, ls + 1100, 500);
    items.forEach((id, k) => appear(id, ls + 1600 + k * 500, 450));
  });
  appear("s2-title", s + 200, 600);
}

// ============================================================
// SCENE 3 - Why it fails (the mechanism)  (~2:00-2:40)
// ============================================================
function scene3() {
  const C = cx(3), s = START[3];
  text("s3-line", C, 150, "It predicts likely text - not true text.", 50, INK, 1400);
  const rows = [
    { id: "calc", icon: "🧮", label: "not a calculator", note: "so: counting, exact maths" },
    { id: "db", icon: "🗄️", label: "not a live database", note: "so: recent facts, niche proprietary knowledge" },
    { id: "rule", icon: "⚙️", label: "not a rule engine", note: "so: deterministic logic, 100% reliability" },
  ];
  rows.forEach((r, i) => {
    const ry = 330 + i * 160;
    text(`s3-${r.id}-ic`, C - 560, ry, r.icon, 60, INK, 100);
    text(`s3-${r.id}-lbl`, C - 230, ry, r.label, 38, INK, 560, "left");
    text(`s3-${r.id}-note`, C + 360, ry, r.note, 24, GREY, 620, "left");
    // strike-through line across icon + label
    line(`s3-${r.id}-strike`, C - 620, ry, [[0, 0], [560, 0]], RED, 5);
  });
  // animation
  appear("s3-line", s + 300, 700);
  rows.forEach((r, i) => {
    const rs = s + 4000 + i * 9000;   // ~2:04, 2:13, 2:22 within the 2:00-2:40 window
    appear(`s3-${r.id}-ic`, rs, 500);
    appear(`s3-${r.id}-lbl`, rs + 300, 500);
    appear(`s3-${r.id}-note`, rs + 700, 500);
    draw(`s3-${r.id}-strike`, rs + 1400, 700);
  });
}

// ============================================================
// SCENE 4 - The unlock: grounding  (~2:40-3:20)
// ============================================================
function scene4() {
  const C = cx(4), s = START[4];
  text("s4-head", C, 110, "Bad at remembering your stuff.\nGood at working with what you give it.", 40, INK, 1400);
  // BEFORE box (left)
  const bx = C - 560;
  rect("s4-before", bx - 150, 280, 300, 200, GREY, WHITE, { strokeWidth: 3 });
  text("s4-before-face", bx, 340, "🤷", 56, INK, 120);
  text("s4-before-txt", bx, 430, "“Don't know your Q3 policy\nor that email thread.”", 20, GREY, 280);
  text("s4-before-lbl", bx, 250, "BEFORE", 22, GREY, 200);
  // document that slides in
  rect("s4-doc", C - 60, 360, 120, 150, BLUE, "#a5d8ff", { strokeWidth: 2 });
  line("s4-docl1", C - 35, 395, [[0, 0], [70, 0]], BLUE, 2);
  line("s4-docl2", C - 35, 420, [[0, 0], [70, 0]], BLUE, 2);
  line("s4-docl3", C - 35, 445, [[0, 0], [50, 0]], BLUE, 2);
  for (const id of ["s4-doc", "s4-docl1", "s4-docl2", "s4-docl3"]) E.find((e) => e.id === id).groupIds = ["s4-docgrp"];
  arrow("s4-arrow", C - 140, 580, [[0, 0], [280, 0]], INK, 3);
  // AFTER box (right)
  const ax = C + 560;
  rect("s4-after", ax - 150, 280, 300, 200, GREEN, "#ebfbee", { strokeWidth: 3 });
  text("s4-after-face", ax, 340, "✅", 56, INK, 120);
  text("s4-after-txt", ax, 430, "drafts it accurately\nfrom your source.", 20, GREEN, 280);
  text("s4-after-lbl", ax, 250, "AFTER", 22, GREEN, 200);
  text("s4-safe", C, 640, "Paste the thread → it summarises it.  Give it the doc → it works from the doc.", 24, GREY, 1300);
  // RED caveat banner (persists)
  rect("s4-caveat-box", C - 700, 720, 1400, 150, RED, TINT_R, { strokeWidth: 3 });
  text("s4-caveat", C, 795, "Grounding fixes recall. It does NOT move anything out of RED.\nDosing, clinical & regulatory calls still need a qualified human - even with the source in front of the AI.", 24, RED, 1340);
  // animation
  appear("s4-head", s + 300, 700);
  for (const id of ["s4-before", "s4-before-face", "s4-before-txt", "s4-before-lbl"]) appear(id, s + 1600, 600);
  appear("s4-after", s + 2400, 500); appear("s4-after-lbl", s + 2400, 500);
  // document slides from before-box into after-box (translateX), then after-box "flips" to accurate
  appear("s4-docgrp", s + 5000, 400);
  kf("s4-docgrp", "translateX", s + 5400, 0, "easeInOut");
  kf("s4-docgrp", "translateX", s + 7400, 480, "easeInOutCubic");   // doc (center C) slides INTO the AFTER box (center C+560)
  // doc is "absorbed" - fades out as it lands, then the box flips to accurate
  kf("s4-docgrp", "opacity", s + 7400, 1);
  kf("s4-docgrp", "opacity", s + 7800, 0, "easeOut");
  draw("s4-arrow", s + 5400, 900);
  appear("s4-after-face", s + 7600, 500);
  appear("s4-after-txt", s + 8000, 500);
  appear("s4-safe", s + 9000, 600);
  // caveat fades up LAST and stays put (no later opacity keyframe)
  appear("s4-caveat-box", s + 12000, 800);
  appear("s4-caveat", s + 12300, 800);
}

// ============================================================
// SCENE 5 - Side-by-side demo  (~3:20-4:00)
// ============================================================
function scene5() {
  const C = cx(5), s = START[5];
  text("s5-title", C, 90, "Same tool. Two very different jobs.", 42, INK, 1200);
  // LEFT panel (good)
  const lx = C - 480, pw = 760, pTop = 190;
  rect("s5-lpanel", lx - pw / 2, pTop, pw, 560, GREEN, WHITE, { strokeWidth: 3 });
  text("s5-lprompt", lx, pTop + 50, "“Summarise this 4-email thread”", 24, INK, pw - 40);
  line("s5-lrule", lx - pw / 2 + 30, pTop + 95, [[0, 0], [pw - 60, 0]], GREEN, 2);
  textL("s5-lb1", lx - pw / 2 + 40, pTop + 160, "• Supplier confirmed Friday delivery", 22, INK, pw - 70);
  textL("s5-lb2", lx - pw / 2 + 40, pTop + 230, "• Two items back-ordered to next week", 22, INK, pw - 70);
  textL("s5-lb3", lx - pw / 2 + 40, pTop + 300, "• Finance needs the revised PO by Mon", 22, INK, pw - 70);
  // green tick (drawProgress)
  line("s5-tick", lx + pw / 2 - 110, pTop + 470, [[0, 0], [30, 36], [80, -60]], GREEN, 8);
  text("s5-lverdict", lx, pTop + 500, "Glance & ship", 24, GREEN, 300);
  // RIGHT panel (wrong on purpose)
  const rx = C + 480;
  rect("s5-rpanel", rx - pw / 2, pTop, pw, 560, RED, WHITE, { strokeWidth: 3 });
  text("s5-rprompt", rx, pTop + 50, "“Calculate exact dosing from\nthis patient record”", 24, INK, pw - 40);
  line("s5-rrule", rx - pw / 2 + 30, pTop + 110, [[0, 0], [pw - 60, 0]], RED, 2);
  text("s5-rans", rx, pTop + 220, "“Give 2.4 mg once weekly,\ntitrate to 4.8 mg next week.”", 24, INK, pw - 60);
  text("s5-rconf", rx, pTop + 320, "(stated with total confidence)", 20, GREY, pw - 60);
  // red cross
  line("s5-cross1", rx + pw / 2 - 110, pTop + 430, [[0, 0], [70, 70]], RED, 8);
  line("s5-cross2", rx + pw / 2 - 40, pTop + 430, [[0, 0], [-70, 70]], RED, 8);
  // stamp (rotates in)
  rect("s5-stamp-box", rx - 170, pTop + 470, 340, 70, RED, "#fff5f5", { strokeWidth: 4, angle: 0 });
  text("s5-stamp", rx, pTop + 505, "Left wrong on purpose", 26, RED, 320);
  for (const id of ["s5-stamp-box", "s5-stamp"]) E.find((e) => e.id === id).groupIds = ["s5-stamp-grp"];
  // animation
  appear("s5-title", s + 200, 600);
  appear("s5-lpanel", s + 1200, 500); appear("s5-rpanel", s + 1200, 500);
  appear("s5-lprompt", s + 1800, 500); appear("s5-rprompt", s + 1800, 500);
  draw("s5-lrule", s + 2200, 500); draw("s5-rrule", s + 2200, 500);
  // left "types out" (opacity, staggered)
  appear("s5-lb1", s + 3000, 500); appear("s5-lb2", s + 3700, 500); appear("s5-lb3", s + 4400, 500);
  // right "types out"
  appear("s5-rans", s + 3300, 600); appear("s5-rconf", s + 4400, 500);
  // verdicts: left tick draws, right cross draws, stamp rotates in
  draw("s5-tick", s + 6000, 700); appear("s5-lverdict", s + 6200, 500);
  draw("s5-cross1", s + 6500, 500); draw("s5-cross2", s + 7000, 500);
  appear("s5-stamp-grp", s + 7600, 400);
  kf("s5-stamp-grp", "rotation", s + 7600, -18);
  kf("s5-stamp-grp", "rotation", s + 8400, -8, "easeOutBack");
  kf("s5-stamp-grp", "rotation", s + 30000, -8);   // stays (no corrected version ever shown)
}

// ============================================================
// SCENE 6 - Your turn (micro-exercise)  (~4:00-4:30)
// ============================================================
function scene6() {
  const C = cx(6), s = START[6];
  text("s6-title", C, 110, "Pick 3 tasks you do every week.", 46, INK, 1200);
  const sheetW = 1200, sheetX = C - sheetW / 2, top = 210;
  rect("s6-sheet", sheetX, top, sheetW, 470, INK, PAPER, { strokeWidth: 3 });
  // column labels
  const colX = [sheetX + 760, sheetX + 940, sheetX + 1110];
  const colLbl = ["Good fit", "Maybe", "Never"];
  const colC = [GREEN, AMBER, RED];
  colLbl.forEach((l, i) => text(`s6-col${i}`, colX[i], top + 50, l, 24, colC[i], 180));
  // 3 rows
  const rowIds = [];
  for (let r = 0; r < 3; r++) {
    const ry = top + 140 + r * 110;
    line(`s6-rowline${r}`, sheetX + 40, ry, [[0, 0], [680, 0]], GREY, 2);
    text(`s6-rownum${r}`, sheetX + 70, ry - 24, `${r + 1}.`, 30, INK, 60);
    rowIds.push(`s6-rowline${r}`, `s6-rownum${r}`);
    // tick boxes
    colX.forEach((bxx, i) => rect(`s6-box${r}-${i}`, bxx - 26, ry - 50, 52, 52, colC[i], WHITE, { strokeWidth: 2 }));
  }
  text("s6-note", C, top + 510, "Keep this list - you'll reuse it in Module 5.", 26, GREY, 900);
  arrow("s6-point", sheetX + 600, top + 90, [[0, 0], [110, 60]], INK, 4);
  // animation
  appear("s6-title", s + 300, 600);
  appear("s6-sheet", s + 1200, 600);
  // rows draw in
  for (let r = 0; r < 3; r++) { draw(`s6-rowline${r}`, s + 2000 + r * 700, 600); appear(`s6-rownum${r}`, s + 2000 + r * 700, 400); }
  // column labels + boxes fade in
  for (let i = 0; i < 3; i++) appear(`s6-col${i}`, s + 4500 + i * 400, 400);
  for (let r = 0; r < 3; r++) for (let i = 0; i < 3; i++) appear(`s6-box${r}-${i}`, s + 5000 + (r * 3 + i) * 150, 350);
  // arrow points at first box
  draw("s6-point", s + 8000, 700);
  appear("s6-note", s + 9000, 600);
}

// ============================================================
// SCENE 7 - Close, accountability & resource  (~4:30-5:00)
// ============================================================
function scene7() {
  const C = cx(7), s = START[7];
  text("s7-close", C, 250, "The skill isn't using AI.\nIt's knowing when.", 64, INK, 1400);
  line("s7-ul", C - 330, 360, [[0, 0], [660, 0]], AMBER, 6);  // underline "knowing when"
  text("s7-acct", C, 480, "In a regulated pharmacy, a qualified human always owns the output.\nAI assists - it never decides, and it's never accountable.", 28, INK, 1300);
  // resource card bottom corner
  rect("s7-card", C + 230, 660, 620, 150, BLUE, "#e7f5ff", { strokeWidth: 3 });
  text("s7-card-t", C + 540, 700, "Read more →", 22, BLUE, 560);
  text("s7-card-b", C + 540, 745, "Ethan Mollick, One Useful Thing (blog)", 24, INK, 580);
  // animation
  appear("s7-close", s + 500, 800);
  draw("s7-ul", s + 1600, 1000);
  appear("s7-acct", s + 3500, 800);
  // resource card slides up from bottom and settles
  appear("s7-card", s + 6000, 500); appear("s7-card-t", s + 6300, 500); appear("s7-card-b", s + 6300, 500);
  for (const id of ["s7-card", "s7-card-t", "s7-card-b"]) { kf(id, "translateY", s + 6000, 160); kf(id, "translateY", s + 7000, 0, "easeOutCubic"); }
}

// ---------- camera pans ----------
function cameraPans() {
  // base frame at scene 1; translateX offsets pan to each scene center
  const holdBefore = 1600;
  const pans = [
    [START[2], 1 * GAP], [START[3], 2 * GAP], [START[4], 3 * GAP],
    [START[5], 4 * GAP], [START[6], 5 * GAP], [START[7], 6 * GAP],
  ];
  const camKf = [{ property: "translateX", time: 0, value: 0 }];
  let prev = 0;
  for (const [t, val] of pans) {
    camKf.push({ property: "translateX", time: t - holdBefore, value: prev });
    camKf.push({ property: "translateX", time: t, value: val, easing: "easeInOutCubic" });
    prev = val;
  }
  camKf.push({ property: "translateX", time: CLIP_END, value: prev });
  return camKf;
}

// ---------- driver ----------
async function main() {
  const cmd = process.argv[2];
  await init();
  if (cmd === "scene1") {
    scene1();
    const out = await call("create_animated_scene", {
      elements: JSON.stringify(E),
      keyframes: JSON.stringify(K),
      cameraFrame: { x: cx(1), y: CY, width: CAM_W, aspectRatio: "16:9" },
      duration: CLIP_END, clipStart: 0, clipEnd: CLIP_END,
    });
    console.log("scene1 ->", out);
  } else if (cmd === "rest") {
    // build scenes 2-7
    scene2(); scene3(); scene4(); scene5(); scene6(); scene7();
    console.log("add_elements ->", await call("add_elements", { elements: JSON.stringify(E) }));
    // keyframes in chunks to keep payloads sane
    for (let i = 0; i < K.length; i += 250) {
      await call("add_keyframes_batch", { keyframes: JSON.stringify(K.slice(i, i + 250)) });
    }
    console.log("keyframes added:", K.length);
    console.log("camera ->", await call("add_camera_keyframes_batch", { keyframes: JSON.stringify(cameraPans()) }));
    console.log("clip ->", await call("set_clip_range", { start: 0, end: CLIP_END }));
  } else if (cmd === "verify") {
    for (let i = 1; i <= 7; i++) {
      const t = START[i] + 12000 <= CLIP_END ? START[i] + (i === 1 ? 9000 : 6000) : START[i] + 2000;
      const vis = await call("items_visible_in_camera", { time: t });
      console.log(`scene ${i} @${t}ms:`, vis);
    }
  } else if (cmd === "finalize") {
    console.log("checkpoint ->", await call("save_checkpoint", { id: "phlo-v1.3-final" }));
    console.log("share ->", await call("share_project", {}));
  } else if (cmd === "dump") {
    const scene = await call("get_scene", {});
    const els = JSON.parse(scene);
    const doc = { type: "excalidraw", version: 2, source: "excalimate", elements: Array.isArray(els) ? els : (els.elements || els), appState: { viewBackgroundColor: "#ffffff", gridSize: null }, files: {} };
    fs.writeFileSync(process.argv[3] || "phlo-ai-1.3.excalidraw", JSON.stringify(doc, null, 2));
    console.log("wrote", process.argv[3] || "phlo-ai-1.3.excalidraw", "elements:", doc.elements.length);
  } else {
    console.log("unknown cmd");
  }
}
main().catch((e) => { console.error(e); process.exit(1); });
