#!/usr/bin/env python3
"""Validate agent JSON: every id must exist in input.json."""

import json
import sys
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    valid_ids = {item["id"] for item in json.loads((here / "input.json").read_text(encoding="utf-8"))}

    if len(sys.argv) != 2:
        print(
            "Usage: python3 validate.py <agent-output.json>\n"
            "       python3 validate.py -   # read JSON from stdin (pipe here-doc)",
            file=sys.stderr,
        )
        sys.exit(2)

    if sys.argv[1] == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(sys.argv[1]).read_text(encoding="utf-8")

    try:
        picked = json.loads(raw.strip())
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}", file=sys.stderr)
        sys.exit(2)

    if not isinstance(picked, list):
        print("Expected a JSON array.", file=sys.stderr)
        sys.exit(2)

    bad = False
    for entry in picked:
        if not isinstance(entry, dict) or "id" not in entry:
            print(f"FAIL: entry must be object with id: {entry!r}", file=sys.stderr)
            bad = True
            continue
        iid = entry["id"]
        if iid in valid_ids:
            print(f"OK:   {iid}")
        else:
            print(f"FAIL: {iid} — not in input.json", file=sys.stderr)
            bad = True

    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
