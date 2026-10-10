# Active Task — M0-A governance corrective checkpoint

Status: **Settings verified; corrective branch checkpoint pending** (2026-10-10)
Milestone: M0
Repository: `Gmpatem/NaboLink`
Branch: `chore/m0-governance-initialization`
Base: remote `main` at `3723c7ab4efa751841a9d5aa6561958079427dd4`; governance branch started M0-A at `74dc843570cf427a54525362da90c3052e0e9047`.

## Scope
Correct four review findings: wrong GitHub default branch, missing main protection, stale remote/CI context, and task-ID validation that rejects `M0-A`. Add focused regression tests, inspect related orientation text and action versions, then validate and push a checkpoint to the existing branch.

## Exclusions
No ISP features, application scaffold, database schema, contract approval, merge, deployment, live payment, or physical router change. Do not alter global Git credentials or unrelated repositories.

## Acceptance
`main` is remotely verified as default; active main protection requires a PR, one approving review, the governance CI check, and blocks deletion and force pushes; branch context matches verified GitHub facts; validator and regression tests pass; the new branch commit is pushed and remote HEAD matches. Report final CI evidence in the completion report rather than embedding a self-referential commit SHA here.

## Next task after M0-A
M0-01: refine the draft residential subscriber lifecycle contract for owner approval. This task is not yet started.
