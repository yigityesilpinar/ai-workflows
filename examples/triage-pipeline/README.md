# Triage pipeline (demo)

Minimal **preview → decide → validate** flow: scripts handle deterministic work; the agent only picks IDs from a bounded preview.

This example shows a simple rule: scripts handle repeatable transformation and validation; the model is used only for judgment.

## How to run this example

1. Run `python3 preview.py` to generate a compact preview of the input items.
2. Copy that preview into `decide_prompt.md` and run the prompt in your model of choice.
3. Save the model output as JSON (for example `picked.json`).
4. Run `python3 validate.py picked.json` to verify that every returned ID exists in `input.json`.

You can also try the included sample: `python3 validate.py picked.example.json`

## Expected outcome

- preview and validation are deterministic  
- the model is used only for selection/judgment  
- invalid IDs fail validation immediately  

| Step | Deterministic? |
|------|----------------|
| preview.py | yes |
| decide (prompt + model) | no — judgment only |
| validate.py | yes |

| File | Role |
|------|------|
| `input.json` | static input items |
| `preview.py` | deterministic preview |
| `decide_prompt.md` | judgment step for the model |
| `validate.py` | deterministic validation |
| `picked.example.json` | sample model output |

See repo patterns [Deterministic First](../../patterns/deterministic-first.md) and [Staged Execution](../../patterns/staged-execution.md).