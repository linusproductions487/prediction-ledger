#!/usr/bin/env python3
"""Independently verify the prediction ledger.

Recomputes every SHA-256 hash from the raw fields and checks every chain link.
Uses only the Python standard library, so you don't have to trust the database,
this repo's automation, or Claude: run it yourself.

    python verify.py ledger.json
"""
import hashlib, json, sys

def h(*fields):
    return hashlib.sha256("|".join(str(f) for f in fields).encode("utf-8")).hexdigest()

def check_predictions(preds):
    prev = "GENESIS"
    for i, p in enumerate(preds, start=1):
        if p["seq"] != i:
            return f"predictions: sequence gap at seq {p['seq']} (expected {i})"
        if p["prev_hash"] != prev:
            return f"predictions: broken link at seq {i}"
        expect = h(p["prev_hash"], p["seq"], p["created_at"], p["topic"], p["claim"],
                   p["resolution_criteria"], p["source_of_truth"], p["confidence"],
                   p["deadline"], p["made_by"], p["rationale"], p["baseline_rule"],
                   p["baseline_confidence"])
        if p["hash"] != expect:
            return f"predictions: content altered at seq {i}"
        prev = p["hash"]
    return None

def check_resolutions(res, preds):
    by_id = {p["id"]: p for p in preds}
    prev = "GENESIS"
    for i, r in enumerate(res, start=1):
        if r["seq"] != i:
            return f"resolutions: sequence gap at seq {r['seq']} (expected {i})"
        if r["prev_hash"] != prev:
            return f"resolutions: broken link at seq {i}"
        p = by_id.get(r["prediction_id"])
        if p is None or p["hash"] != r["prediction_hash"]:
            return f"resolutions: seq {i} points to a missing or altered prediction"
        if r["resolved_at"] < p["created_at"]:
            return f"resolutions: seq {i} resolved before its prediction existed"
        expect = h(r["prev_hash"], r["seq"], r["prediction_id"], r["prediction_hash"],
                   r["outcome"], r["evidence_url"], r["notes"], r["resolved_at"])
        if r["hash"] != expect:
            return f"resolutions: content altered at seq {i}"
        prev = r["hash"]
    return None

def check_against_history(data, anchors_path="ANCHORS.md"):
    """Every hash ever anchored must still exist in the chain (catches rewrites)."""
    try:
        lines = open(anchors_path, encoding="utf-8").read().splitlines()
    except FileNotFoundError:
        return None
    hashes = {p["hash"] for p in data["predictions"]} | {r["hash"] for r in data["resolutions"]}
    for line in lines:
        parts = [x.strip() for x in line.split("|")]
        if len(parts) >= 6 and len(parts[3]) == 64 and parts[3] not in hashes:
            return f"previously anchored hash {parts[3][:12]}... is missing from the chain"
        if len(parts) >= 6 and len(parts[5]) == 64 and parts[5] not in hashes:
            return f"previously anchored hash {parts[5][:12]}... is missing from the chain"
    return None

def main(path):
    data = json.load(open(path, encoding="utf-8"))
    errors = [e for e in (
        check_predictions(data["predictions"]),
        check_resolutions(data["resolutions"], data["predictions"]),
        check_against_history(data),
    ) if e]
    if errors:
        print("LEDGER INVALID"); [print(" -", e) for e in errors]; sys.exit(1)
    print(f"LEDGER VALID: {len(data['predictions'])} predictions, "
          f"{len(data['resolutions'])} resolutions, all hashes and links check out.")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "ledger.json")
