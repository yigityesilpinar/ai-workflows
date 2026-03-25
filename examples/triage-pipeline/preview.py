#!/usr/bin/env python3
"""Deterministic preview: compact, bounded view of input.json (no AI)."""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    path = here / "input.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)

    print("ID      | Subject (truncated)                    | From                     | Age")
    print("--------|----------------------------------------|--------------------------|-----")
    for item in data:
        subj = item["subject"][:38] + ("…" if len(item["subject"]) > 38 else "")
        received = datetime.fromisoformat(item["received"].replace("Z", "+00:00"))
        age_days = (now - received).days
        age = f"{age_days}d" if age_days else "<1d"
        frm = item["from"][:24] + ("…" if len(item["from"]) > 24 else "")
        print(f"{item['id']:7} | {subj:38} | {frm:24} | {age:>3}")


if __name__ == "__main__":
    main()
