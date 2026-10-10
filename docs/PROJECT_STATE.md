# Canonical Project State

Updated: 2026-10-10
Stage: **M0 — Planning / governance correction**
Implementation: **Not started**
Hardware: **None purchased**
Deployment: **None**
Repository: `Gmpatem/NaboLink` (`https://github.com/Gmpatem/NaboLink.git`)
Integration branch: `main` at verified remote SHA `3723c7ab4efa751841a9d5aa6561958079427dd4`
Working branch: `chore/m0-governance-initialization`
Active task: M0-A governance corrective checkpoint in `docs/tasks/ACTIVE_TASK.md`.

## Verified remote status
The `main` baseline and governance branch were pushed. The M0-A corrective code checkpoint `761fd2cae2faaf2f7b1861155f6794a319d1c547` was pushed and its Governance Checks run succeeded, including task-ID regression tests. Remote synchronization is established and the earlier HTTP 403 blocker is resolved. GitHub names `main` as default and reports it protected: PR with one approving review, required `governance` check, admin enforcement, and deletion/force-push disabled. These settings were read back through the GitHub API. Authorized Gmpatem access was used without changing the globally active account. The final branch SHA is reported after the handoff update is pushed.

## Confirmed direction
- Build before buying equipment; mock, then CHR/RADIUS lab, then approved physical commissioning.
- Distinct residential subscription and public Wi-Fi voucher policies; initial 100-subscriber Cameroon target.
- Keep financial truth, entitlement, desired access, applied policy, and observed connectivity separate.
- Protect customer data with server and database authorization and traceable changes.

## Proposed, not approved
- Exact stack and runtime beyond preliminary architecture, commercial plans, MoMo provider, role matrix, outage policy, schema, and state transitions.
- Subscriber lifecycle contract and ADR-0001 remain draft/proposed. No product implementation is authorized by them.
- Repository vision/principles copies are version 1.0 and marked proposed. Their versions against the actual ChatGPT Project Sources remain unverified; do not overwrite the sources based on this repository copy.

## Gate and next action
**M0 contract gate has not passed.** M0-A corrections are ready for independent review; integration remains subject to the required PR review and separate owner approval. M0-01 subscriber lifecycle contract work remains pending. No application code, deployment, real payment or physical router validation has occurred.
