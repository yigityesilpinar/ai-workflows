# Example — Project Instructions for Agents (Sample)

Fictional project. Replace names and commands with yours. Keep the **shape**: short root file, link-outs for detail.

---

## `AGENTS.md` (root)

```markdown
# Example Service

Python API + Postgres. Agents run tests before claiming work is done.

## Commands

- Install: `make setup`
- Tests: `make test`
- Lint: `make lint`

## Boundaries

- Do not commit secrets or `.env` files.
- API changes need a note in `docs/CHANGELOG.md` and a test under `tests/api/`.
- Prefer small PR-sized changes; ask before schema migrations.

## Layout

- `src/` — application code
- `tests/` — tests mirror package layout
- `docs/` — architecture notes; read `docs/architecture.md` before large refactors
```

---

## What this encodes (checklist)

| Section | Why |
|---------|-----|
| One-line identity | Orients any agent or human quickly |
| Commands | Reduces invented build steps |
| Boundaries | Non-negotiables and safety |
| Layout + pointer | Progressive disclosure without a 300-line file |

---

## What to avoid here

- Tutorial content that duplicates the README  
- Style rules already enforced by formatters  
- Secrets, production URLs, or internal-only runbooks  

---

## Optional: area-specific file

`src/ingestion/AGENTS.md` (lazy-loaded when working in that tree):

```markdown
# Ingestion

- Batch jobs are idempotent; use the idempotency key in the job table.
- Do not delete rows from `raw_events`; mark `superseded_at` instead.
```

Narrow rules beat global vagueness.
