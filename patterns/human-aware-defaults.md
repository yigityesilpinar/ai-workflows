# Human-Aware Defaults

AI that is technically correct but hard to trust or verify will not be used.

Most adoption failures are human, not technical: trust, cognitive load, unclear ownership, and iteration fatigue. Workflows should be designed for how people actually verify and delegate — not for an idealized “fully automated” user.

---

## Problem

| Failure mode | What goes wrong |
|--------------|-----------------|
| Trust gap | Output looks plausible; nobody knows how to check it, so they redo work by hand |
| Review overload | “Verify this wall of text” costs more attention than doing the task |
| Iteration fatigue | Fixing the model’s mistakes round after round feels worse than starting alone |
| Hidden reasoning | No sense of *why* the system chose what it chose, so confidence never grows |

---

## Pattern

Design defaults that reduce verification cost and increase justified trust:

1. **Preview before mutate** — show what will change; require explicit go-ahead for irreversible steps.  
2. **Small chunks** — fewer, smaller outputs beat one huge generation.  
3. **Visible reasoning when it matters** — short “here’s what I’m doing and why” before long execution.  
4. **Loud failures with next steps** — silent failure kills trust; a clear error and one or two fixes preserves it.  
5. **Pace to the verifier** — don’t automate faster than a human can sanely check.

---

## Decision rule

> If the model is wrong here, how expensive is it for a human to notice, understand, and fix?

- **Expensive** → narrow scope, preview, split steps, show reasoning.  
- **Cheap** → you can automate more aggressively.

---

## Tradeoffs

| Benefit | Cost |
|---------|------|
| Higher real adoption | Throughput can look slower on demos |
| Trust compounds over time | More design work than “ship the prompt” |
| Less rework from late surprises | Extra clicks or confirmations |

---

## Example

**Bad:** Auto-file every generated document into the system of record with no diff or summary.  
**Better:** Write to a staging area, show a one-screen diff or checklist, then commit. The human’s job stays bounded.
