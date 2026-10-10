# Community ISP — Agent Rules (mandatory)

Read `chatgpt-project/PROJECT_VISION.md`, `chatgpt-project/PROJECT_PRINCIPLES.md`, and `docs/REMOTE_CONTEXT_AND_BRANCH_POLICY.md` first. Follow `docs/PROJECT_STATE.md`, `docs/tasks/ACTIVE_TASK.md`, `docs/DECISION_LOG.md`, approved `docs/contracts/`, ADRs and the last verified handoff. Inspect actual code before editing.

**Innovation is welcome** as an isolated experiment, proposal or scoped feature. Stable customer/business contracts are not silently editable. Do not start product implementation during M0 without owner approval of its governing contract; planning, prototyping and simulator spikes can remain nonproduction.

For an approved task: inspect branch, remote, SHA and tree; state scope and tests; implement a small vertical slice; validate; update state and handoff; commit and push a meaningful checkpoint to the authorized **feature branch**; verify remote HEAD. No repetitive approval needed for ordinary feature-branch pushes. Mark failed checks/WIP honestly. Do not claim an unverified push happened.

No merging, protected-main push, deployment, destructive migration, live payment or physical router change without separate explicit authorization. No secrets or PII in committed context. Differentiate payment verification, subscription entitlement, desired access, applied router policy and actual session observations. Enforce server/database authorization, traceable changes and safe recovery. Never claim mocked infrastructure equals physical validation.

See `docs/REMOTE_CONTEXT_AND_BRANCH_POLICY.md` for mandatory synchronization steps and `docs/ENGINEERING_PLAYBOOK.md` for development quality gates.
