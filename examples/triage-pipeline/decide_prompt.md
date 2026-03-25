# Triage — select IDs (agent step)

You are **only** choosing which item IDs need human attention today. You are not summarizing inboxes or inventing work.

## Input

Paste the **exact** output of `python3 preview.py` (the table) below. Use only the preview for selection. Refer to `input.json` only if a preview row is ambiguous.

```
[PASTE PREVIEW TABLE HERE]
```

## Task

Return **only** JSON (no markdown fences, no prose) with this shape:

```json
[
  {"id": "E-001", "reason": "one short line why this needs attention"}
]
```

## Rules

- Include **only** IDs that appear in the preview for this run.
- Do **not** add IDs not in the input.
- Do **not** summarize unrelated items.
- If nothing needs attention, return `[]`.

## Output

Single JSON array only.

Afterward, save that JSON to a file (e.g. `picked.json`) and run `python3 validate.py picked.json`. To try validation without a model, use the repo’s sample output: `python3 validate.py picked.example.json`. Or pipe: `… | python3 validate.py -`.
