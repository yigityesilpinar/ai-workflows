# Cost as Constraint

Token usage is not a billing footnote; it shapes behavior, latency, and failure modes. Treat it like memory or latency: a first-class constraint on design.

---

## Problem

If cost is ignored until the bill arrives, you get:

- Huge context loads “for completeness”  
- Models doing work scripts should do  
- Unbounded list outputs and chat dumps  
- No default guardrails on expensive or irreversible calls  

---

## Pattern

| Lever | What to do |
|-------|------------|
| **Prefer narrow context** | Search, then read slices; don’t paste whole repos or logs into chat |
| **Cap list outputs** | Default limits on how many items or how much text a step returns |
| **Artifacts, not chat** | Large results go to files; the agent sees paths and short previews |
| **Safe defaults for paid steps** | Assume dry-run or preview unless the user opts in |
| **Batch outside the model** | Parallelize deterministic work in scripts, not in N serial chat turns |

---

## Decision rule

For any step that invokes a model or a paid API:

> What is the smallest input and smallest output that still allows a correct decision?

If you cannot answer that, the step is underspecified.

---

## Tradeoffs

| Benefit | Cost |
|---------|------|
| Predictable spend | You must design interfaces and caps up front |
| Faster iteration (less noise) | Occasional extra round trip to fetch detail |
| Fewer “runaway” sessions | Some convenience features stay behind explicit flags |

---

## Example

**Bad:** “Here is the entire 400 KB log; summarize.”  
**Better:** Script extracts error lines and stack tops into a 40-line file; the model summarizes that. Same insight, orders of magnitude fewer tokens.
