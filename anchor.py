#!/usr/bin/env python3
"""Normalize the export, append a new anchor row if the chain moved, and rebuild SCORECARD.md."""
import json, sys, datetime

raw = json.load(open("raw.json", encoding="utf-8"))
raw.pop("exported_at", None)          # keep ledger.json byte-stable between runs
json.dump(raw, open("ledger.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
open("ledger.json", "a").write("\n")

preds, res = raw["predictions"], raw["resolutions"]
p_head = preds[-1]["hash"] if preds else "-"
r_head = res[-1]["hash"] if res else "-"

# --- ANCHORS.md (append-only) ---
lines = open("ANCHORS.md", encoding="utf-8").read().rstrip("\n").splitlines()
last = [x.strip() for x in lines[-1].split("|")] if lines else []
if len(last) < 6 or last[2] != str(len(preds)) or last[4] != str(len(res)) or last[3] != p_head or last[5] != r_head:
    if preds or res:
        now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        lines.append(f"| {now} | {len(preds)} | {p_head} | {len(res)} | {r_head} |")
        open("ANCHORS.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")

# --- SCORECARD.md ---
resolved_ids = {r["prediction_id"]: r for r in res}
pending = [p for p in preds if p["id"] not in resolved_ids]
scored = [(p, resolved_ids[p["id"]]) for p in preds
          if p["id"] in resolved_ids and resolved_ids[p["id"]]["outcome"] != "void"]
voids = sum(1 for r in res if r["outcome"] == "void")

out = ["# Scorecard", "",
       "Generated automatically from the ledger. Every miss is included.", "",
       f"- Predictions made: **{len(preds)}**",
       f"- Resolved (scored): **{len(scored)}**  ·  Void: **{voids}**  ·  Pending: **{len(pending)}**"]

if scored:
    brier = sum((p["confidence"]/100 - (1 if r["outcome"] == "true" else 0))**2 for p, r in scored) / len(scored)
    # "right" = the side Claude leaned toward happened
    right = sum(1 for p, r in scored if (p["confidence"] > 50) == (r["outcome"] == "true") and p["confidence"] != 50)
    out += [f"- Leaned the right way: **{right}/{len(scored)}**",
            f"- Brier score: **{brier:.4f}** (0 = perfect, 0.25 = coin flip, lower is better)", ""]
    if raw.get("calibration"):
        out += ["## Calibration", "",
                "When I say X%, does it happen X% of the time?", "",
                "| Confidence band | Predictions | Stated | Actually true |", "|---|---|---|---|"]
        for c in raw["calibration"]:
            out.append(f"| {c['band_start']}–{c['band_start']+9}% | {c['n']} | {c['stated_pct']}% | {c['actual_pct']}% |")
        out.append("")
    if raw.get("scorecard_by_topic"):
        out += ["## By topic", "", "| Topic | Resolved | Brier |", "|---|---|---|"]
        for t in raw["scorecard_by_topic"]:
            out.append(f"| {t['topic']} | {t['resolved']} | {t['brier_score']} |")
        out.append("")
    out += ["## Resolved", "", "| # | Claim | Confidence | Outcome |", "|---|---|---|---|"]
    for p, r in sorted(scored, key=lambda x: -x[1]["seq"]):
        mark = "✅" if (p["confidence"] > 50) == (r["outcome"] == "true") else "❌"
        out.append(f"| {p['seq']} | {p['claim'].replace('|','/')} | {p['confidence']}% | {mark} {r['outcome']} |")
    out.append("")
else:
    out.append("")

if pending:
    out += ["## Pending", "", "| # | Claim | Confidence | Deadline (UTC) |", "|---|---|---|---|"]
    for p in sorted(pending, key=lambda x: x["deadline"]):
        out.append(f"| {p['seq']} | {p['claim'].replace('|','/')} | {p['confidence']}% | {p['deadline'][:10]} |")
    out.append("")

open("SCORECARD.md", "w", encoding="utf-8").write("\n".join(out))
