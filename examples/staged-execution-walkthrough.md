# Example — Staged Execution (Fictional)

Domain-agnostic walkthrough: **preview → capture → resolve**. No real tools or credentials.

---

## Setting

You pull work items from a remote queue (tickets, emails, tasks — same shape).

---

## Stage 1 — Preview

**Goal:** See what exists; cap noise.

**Script or tool output (example):**

| ID | Title | Age |
|----|-------|-----|
| Q-1042 | Export fails on large tables | 2d |
| Q-1043 | Button color contrast | 5d |

**Gate:** Human or agent picks **one** ID to process next. No fetch of full bodies yet.

---

## Stage 2 — Capture

**Goal:** Persist the full artifact locally before mutating source state.

**Action:** For `Q-1042`, fetch full thread + attachments into a folder:

```text
work/Q-1042/
  thread.md      # human-readable
  meta.json      # ids, timestamps, hashes
```

**Gate:** Confirm files exist and `meta.json` has a content hash. If capture fails, **do not** run resolve.

---

## Stage 3 — Resolve

**Goal:** Mark the item handled in the source system only after capture succeeded.

**Action:** Call “mark processed” for `Q-1042`.

**Gate:** If the API errors, surface the error; do not claim done.

---

## Where the model helps

| Step | Model? |
|------|--------|
| Choose which ID to tackle next | Often yes (prioritization) or human |
| Run preview/capture/resolve scripts | No — deterministic |
| Summarize `thread.md` for a handoff | Yes — small input, bounded output |

---

## Anti-pattern

Skipping preview and asking the model to “process all open items” in one shot. You lose caps, provenance, and a safe place to inspect before resolve.
