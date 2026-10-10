# Remote Context and Branch Checkpoint Policy

Canonical repository: `https://github.com/Gmpatem/NaboLink.git`. `main` is the integration branch. The active task names the authorized working branch. `docs/CONTEXT_SYNC_PROTOCOL.md` is a compatibility pointer to this file.

## Stable vs live knowledge
- ChatGPT Project sources: `chatgpt-project/PROJECT_VISION.md` and `PROJECT_PRINCIPLES.md`. Upload these once to the ChatGPT Project; they are deliberately stable.
- GitHub is canonical for implementation. Prefer branch-specific `docs/PROJECT_STATE.md`, `docs/tasks/ACTIVE_TASK.md`, `docs/handoffs/LATEST.md`, relevant contracts and ADRs, code and tests.
- Fetch actual remote branch HEAD before advising on current implementation. If inaccessible, mark unverified. Do not assume `main` incorporates feature branches.

## Agent startup
1. Check actual repo, branch, remote tracking branch, status, head SHA and last commit.
2. Read `AGENTS.md`, state, active task, decision log, applicable contracts and handoff on the current branch.
3. Check the actual implementation and tests; stop and surface meaningful disagreements.
4. Work only within approved task and written contracts. Experiments are welcome as isolated spikes or marked WIP.

## Mandatory meaningful checkpoint
1. Run relevant checks; report failures and unknowns truthfully.
2. Update branch-scoped project state, decisions only when approved, and latest handoff.
3. Commit with meaningful description.
4. Push **the designated development branch**, not automatically `main`.
5. Confirm remote ref points to intended commit; report full SHA and link.
6. If tests fail, use WIP status and explain problems; no falsely successful handoff.

Checkpoint means coherent feature slice, useful investigation conclusion, approved contract, or prepared handoff — not every keystroke. Don't accumulate hours of unpushed work. If credentials/network are unavailable, report the unsynced checkpoint explicitly.

## Protected operations
Pushing to authorized feature branches does not require repetitive consent. Merging/PR approval, pushing directly to protected main, release/deployment, destructive migrations, live payments, and actual router changes do require explicit task-specific approval.

## Branch truth
A feature branch's project state describes that branch only. Main's state describes integrated features only. Draft PRs may expose changes for review; opening one is not approval to merge. Do not invent commit IDs in a file before commit creation.

## Handoff fields
Repository • feature branch • base branch • starting SHA • latest known local SHA (or pending before commit) • push result and remote SHA (reported after push, never guessed) • milestone • active task • changed files • approved scope • test commands/results • blockers • incomplete items • contract impact • next authorized step.

## Ownership of live context
`docs/PROJECT_STATE.md` owns milestone, implementation status and next action. `docs/tasks/ACTIVE_TASK.md` owns authorized scope and branch. `docs/DECISION_LOG.md`, ADRs and contracts own decision and approval status. `docs/handoffs/LATEST.md` records checkpoint evidence. Git and the remote ref own commit SHAs; report the final remote SHA after pushing rather than amending a committed handoff to include itself. Do not duplicate the full policy in another document.
