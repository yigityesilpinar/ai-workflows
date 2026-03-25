# Staged Execution

---

## Problem

End-to-end “do the whole thing” requests hide mistakes until the end. Large outputs are hard to review. Side effects run before anyone confirms intent.

---

## Pattern

Structure work in **three stages** with explicit gates:

| Stage | Purpose | Typical output |
|-------|---------|----------------|
| **Preview** | Show what exists and what would happen | IDs, titles, counts, dry-run plan |
| **Capture** | Persist full content in a durable place | Files or records with clear paths |
| **Resolve** | Mark source state or close the loop | “Done”, archived, sent — explicit completion |

Internally you might think “list → materialize → complete.” The external name is **staged execution**: each stage is a checkpoint.

---

## Decision rule

Use staged execution when:

- There is an external system (inbox, API, queue) and you must avoid blind writes.  
- Output size or cost would explode if you skipped preview.  
- You need provenance: what was pulled, when, and what changed afterward.

Skip it when the task is tiny, fully local, and reversible in one step.

---

## Tradeoffs

| Benefit | Cost |
|---------|------|
| Errors surface early | Extra steps and UI friction |
| Auditable trail | More design than a single prompt |
| Safer automation | Slower “happy path” if you over-stage trivial work |

---

## Example

**Support tickets:** Preview = list open tickets (capped). Capture = pull full thread to a folder per ticket. Resolve = mark processed in the source system only after capture succeeds.

The agent’s job is to pick *which* ticket to process and to summarize — not to replace the pipeline.
