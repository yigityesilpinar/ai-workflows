# Triage pipeline (demo)

Minimal **preview → decide → validate** flow: scripts handle deterministic work; the agent only picks IDs from a bounded preview.

This example shows a simple rule: scripts handle repeatable transformation and validation; the model is used only for judgment.

1. `python3 preview.py` — read `input.json`, print a capped table (no AI).  
2. Paste the table into `decide_prompt.md` as instructed, run that prompt in your agent. Save the model’s reply as JSON (e.g. `picked.json` — any filename is fine).  
3. `python3 validate.py picked.json` **or** `echo '[...]' | python3 validate.py -` — validates every `id` against `input.json`. Try the included sample: `python3 validate.py picked.example.json`.

| Step | Deterministic? |
|------|----------------|
| preview.py | yes |
| decide (prompt + model) | no — judgment only |
| validate.py | yes |

See repo patterns [Deterministic First](../../patterns/deterministic-first.md) and [Staged Execution](../../patterns/staged-execution.md).

| File | Role |
|------|------|
| `input.json` | static input items |
| `preview.py` | deterministic preview |
| `decide_prompt.md` | judgment step for the model |
| `validate.py` | deterministic validation |
| `picked.example.json` | sample model output |
