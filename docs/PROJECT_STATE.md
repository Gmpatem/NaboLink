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
The `main` baseline and governance branch were pushed. At the start of M0-A, the governance branch remote HEAD was `74dc843570cf427a54525362da90c3052e0e9047`, two commits ahead of `main`. Governance Checks succeeded on both refs. Remote synchronization was established and the earlier HTTP 403 blocker was resolved. GitHub now names `main` as default and reports it protected: PR with one approving review, required `governance` check, admin enforcement, and deletion/force-push disabled. These settings were read back through the GitHub API. The new M0-A branch checkpoint and CI run are pending; authorized Gmpatem access is available without changing the globally active account.

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
**M0 contract gate has not passed.** Push and verify the M0-A corrective checkpoint and CI before independent review; integration remains subject to owner approval. M0-01 subscriber lifecycle contract work remains pending. No application code, deployment, real payment or physical router validation has occurred.
