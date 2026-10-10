# NaboLink — Agent Rules (mandatory)

Canonical repository: `https://github.com/Gmpatem/NaboLink.git` (`Gmpatem/NaboLink`). Work from `E:\NaboLink`. `main` is the integration branch. Current task and authorized working branch are in `docs/tasks/ACTIVE_TASK.md`.

Read `chatgpt-project/PROJECT_VISION.md`, `chatgpt-project/PROJECT_PRINCIPLES.md`, and `docs/REMOTE_CONTEXT_AND_BRANCH_POLICY.md` first. Then inspect Git status, remotes, local and remote branch SHAs, recent commits, `docs/PROJECT_STATE.md`, `docs/tasks/ACTIVE_TASK.md`, `docs/DECISION_LOG.md`, approved contracts and ADRs, `docs/handoffs/LATEST.md`, and actual code and tests. If the remote cannot be verified, say so; never treat a chat summary as current repository truth.

Work within the approved task. Before changing product behavior, identify its governing approved contract, affected permissions, failure cases, and verification plan. During M0, product implementation requires owner approval of its governing contract. Isolated planning, prototypes, and simulator experiments may remain explicitly nonproduction. Preserve accepted decisions; propose amendments rather than silently changing them.

Use small, reversible vertical slices. Enforce server and database authorization, traceable changes, and safe recovery. Distinguish verified payment, subscription entitlement, desired access, applied router policy, and observed sessions. Never claim simulation proves physical behavior or that a requested network action was applied.

At a meaningful checkpoint, run applicable checks, update branch-scoped project state and the latest handoff, commit together, push the designated `chore/*`, `docs/*`, `feature/*`, `fix/*`, or `experiment/*` branch, and verify its remote HEAD SHA. Authorized feature-branch pushes need no repeated approval. Mark incomplete work and failed checks as WIP. Do not claim an unverified push happened. The SHA of a commit cannot be embedded in that same commit; report the final verified remote SHA after pushing.

Do not merge, push to protected `main`, deploy, run destructive migrations or live payments, or change a physical router without separate explicit authorization. Never commit secrets or customer PII. See `docs/ENGINEERING_PLAYBOOK.md` for quality gates.
