# ai-workflows

Most AI-assisted work fails not because models are weak, but because the interaction between human, agent, and system is unstructured.

This is not about using AI more.  
It's about making AI-assisted work reliable, debuggable, and usable by real people.

These patterns are for designing that interaction layer: coordination over generation, structure over prompting, scripts for deterministic work and agents for ambiguity.

---

## Patterns

| # | Pattern | One-line idea |
|---|---------|---------------|
| 1 | [Deterministic First](patterns/deterministic-first.md) | Deterministic work should not use tokens. |
| 2 | [Staged Execution](patterns/staged-execution.md) | Preview, capture, resolve — gates at each stage. |
| 3 | [Human-Aware Defaults](patterns/human-aware-defaults.md) | Adoption fails on trust and cognitive load, not only on model quality. |
| 4 | [Cost as Constraint](patterns/cost-as-constraint.md) | Token usage is a design variable. |
| 5 | [Constrained Agents](patterns/constrained-agents.md) | Agents need boundaries, not open-ended freedom. |

---

## Non-Goals

This is not:

- a prompt collection  
- an agent framework  
- a tool to install  

This is a set of patterns for thinking about AI-assisted work.

---

## Examples

- [Staged execution walkthrough](examples/staged-execution-walkthrough.md)
- [Sample project instructions for agents](examples/sample-agents-md.md)
- [Triage pipeline — runnable example](examples/triage-pipeline/)

---

## Context

Distilled from real daily use of AI-assisted development workflows — not theory, not a product pitch.

---

## License

MIT — see [LICENSE](LICENSE).
