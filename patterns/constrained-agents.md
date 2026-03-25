# Constrained Agents

Agents do better with **clear boundaries** than with open-ended freedom. Constraints reduce hallucination, inconsistency, and unsafe side effects — and they make automation reviewable.

---

## Problem

Unconstrained agents:

- Invent commands, paths, or policies that don’t exist  
- Drift from repo conventions  
- Take destructive actions without a defined checkpoint  
- Burn context repeating things that belong in a short rule  

“Just be helpful” is not an operating model.

---

## Pattern

Encode constraints where the agent will actually read them:

| Mechanism | Role |
|-----------|------|
| **Short project instructions** | Non-negotiables: how to build, test, what not to touch |
| **Scoped rules** | Deeper detail in separate files; load by area, not one giant blob |
| **Explicit allow/deny** | What tools or side effects are permitted without asking |
| **Parseable outputs** | When the next step is a script, require a format machines can consume |

Principles: **progressive disclosure** (essentials first, detail on demand), **fewer sharper rules** over many vague ones, **update when the same mistake repeats**.

---

## Decision rule

> Would removing this constraint cause a repeated class of mistakes?

If yes, keep it. If no, delete it. Stale rules erode trust in all rules.

---

## Tradeoffs

| Benefit | Cost |
|---------|------|
| More predictable agent behavior | Time to write and maintain rules |
| Easier review of automated changes | Can feel “heavy” for throwaway experiments |
| Alignment with team conventions | Duplication if docs and code diverge |

---

## Example

**Bad:** “Use good judgment when changing the API.”  
**Better:** “Public API changes require a changelog entry and a test in `tests/api/`; do not rename fields without a deprecation note.”  
Concrete, checkable, boring — in a good way.
