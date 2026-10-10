# Active Task — GOV-002 M0 governance initialization

Status: **Local checkpoint ready; remote sync blocked by GitHub permission** (2026-10-10)
Repository: `Gmpatem/NaboLink`
Branch: `chore/m0-governance-initialization`
Base: local `main` baseline `3723c7ab4efa751841a9d5aa6561958079427dd4`; remote was verified empty before initialization.

## Scope
Align NaboLink identity and agent instructions; preserve existing planning history; establish Git baseline and branch policy; make status and handoff accurate; add lightweight governance validation and GitHub Actions; validate, commit, push and verify the authorized feature branch.

## Exclusions
No ISP application scaffold or features, contract approval, cloud deployment, database mutation, live payment, physical network change, merge, or protected-main push.

## Acceptance
Governance validator and CI configuration are checked locally; no obvious secrets or application code are staged; branch and remote state are reported accurately; the authorized branch is pushed and its remote HEAD verified if credentials and network allow. If push is blocked, record an unsynced checkpoint and the exact blocker.

## Next task after GOV-002
M0-01: refine the draft residential subscriber lifecycle contract and obtain owner approval before any production implementation.
