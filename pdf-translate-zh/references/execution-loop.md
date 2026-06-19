# Anti-Stall Execution Loop

Use this protocol before and alongside the translation quality loop. Its purpose is to prevent status-message loops, repeated planning, and long periods without artifacts.

## Execution State

Maintain a small state file in the work directory:

```yaml
stage: inventoried | calibrated | translating | drafted | rendered | repairing | passed
last_verified_output: "<path, command result, or QA finding>"
next_action: "<single executable action>"
stall_count: 0
updated_at: "<timestamp>"
```

Update it after every meaningful tool result. Resume from `next_action`, not from a newly narrated plan.

## Valid Progress

At least one of these must occur during a working turn:

- a source inventory, extraction, glossary, translation checkpoint, script, DOCX, render, or QA record is created or updated;
- a command produces information that changes the next action;
- a real error or permission blocker is captured with its exact message;
- a failed QA item is repaired and rechecked.

Plans, promises, repeated summaries, and “正在生成” messages are not progress.

## Turn Contract

1. Send at most one concise progress update before acting.
2. Perform the next executable action in the same turn.
3. Continue through dependent actions when feasible; do not stop merely because one step completed.
4. End the turn only with:
   - a completed deliverable;
   - a concrete blocker that cannot be resolved locally.
5. Never leave a required command session running when ending the turn.

If the user says “继续”:

1. Read the state file or inspect existing artifacts.
2. Execute `next_action` immediately.
3. Do not repeat the plan, apologize again, or request another “继续”.

## First-Artifact Deadline

Create a tangible artifact as early as technically possible:

- short-form: complete first draft after source inspection;
- long-form: output shell plus first accepted section;
- mixed-source guide: structured outline plus translated representative sections;
- scan-heavy: OCR checkpoint plus first verified translated page.

Calibration may block bulk production, but it must not expand into indefinite analysis. Once the representative sample passes, create the artifact immediately.

## Stall Detection

Increment `stall_count` when a working turn produces no valid progress.

- `stall_count = 1`: skip further explanation and execute the smallest useful action.
- `stall_count = 2`: activate recovery; create the minimum viable artifact immediately.
- `stall_count >= 3`: stop all optional work, inspect the filesystem and exact errors, then complete the shortest path to a deliverable or report the concrete blocker.

Reset `stall_count` to zero whenever valid progress occurs.

## Recovery Procedure

1. Inspect current files and processes.
2. Identify the smallest artifact that proves forward motion.
3. Create it with the simplest reliable method.
4. Save state.
5. Continue quality improvement from that artifact.

Examples:

- Write and run the DOCX builder instead of describing its future structure.
- Save one accepted translated section instead of repeatedly refining the full plan.
- Render the existing DOCX instead of discussing anticipated layout defects.
- Record the exact command error instead of saying that the tool “seems blocked”.

## Communication Guardrails

- Do not send multiple consecutive status-only messages.
- Do not say “the next action will be...” unless that action is also executed in the same turn.
- Do not ask for confirmation for routine, reversible work already covered by the request.
- Report progress in terms of concrete outputs: file paths, accepted sections, page counts, render results, or exact blockers.
- After an interruption or context transition, inspect artifacts before speaking so the newest message resumes actual work.
