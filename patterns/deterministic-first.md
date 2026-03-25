# Deterministic First

This pattern is the foundation for making AI-assisted systems predictable.

---

## Problem

The default is to let the agent fetch data, transform it, write files, and decide what comes next. Most of that work is repeatable: same inputs → same outputs. Running it through a model burns tokens, adds variance, and is harder to debug than a script.

---

## Pattern

Split the workflow into two layers:

| Layer | Handles | Properties |
|-------|---------|------------|
| **Deterministic** | Fetch, parse, format, validate, write to disk | No tokens; repeatable; testable |
| **Ambiguous** | Judgment, planning, novel situations, human-facing wording | Model; variable |

The agent **orchestrates** (what step next, what needs judgment). **Scripts execute** the mechanical parts.

---

## Decision rule

Before giving work to a model, ask:

> Would this produce the same output every time for the same input?

- **Yes** → script or CLI, not the model.  
- **No** → model (or human).  
- **Partly** → split: script the deterministic slice, then call the model on the remainder.

---

## Tradeoffs

| Benefit | Cost |
|---------|------|
| Lower cost, predictable behavior | Up-front time to define scripts and interfaces |
| Easier debugging and caching | More moving parts than “agent does everything” |
| Clear boundaries for tests | Wrong if you over-script exploratory one-offs |

**When to relax:** one-off exploration, pure creative work, or early prototyping where structure would slow you down without teaching you much.

---

## Example

**Bad:** “Pull my open items, normalize them, save to a file, then tell me what to do tomorrow.”  
Most steps are mechanical; only “what matters tomorrow” might need judgment.

**Better:** A small script lists and normalizes items and writes a summary path. The model (or you) reads that summary and decides priorities — one ambiguous step, not five.
