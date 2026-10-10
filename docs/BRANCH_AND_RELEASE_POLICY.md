# Branch and Release Policy

- `main` is the reviewed integration baseline. On 2026-10-10, GitHub API readback verified it as the default protected branch: PR with one approving review, required `governance` check, admin enforcement, and deletion/force-push disabled. Recheck GitHub before relying on these settings in a later session.
- Use short-lived `chore/*`, `docs/*`, `feature/*`, `fix/*`, or `experiment/*` branches for focused work. M0 initialization uses `chore/m0-governance-initialization`.
- Commit and push meaningful checkpoints to the authorized task branch, then verify its remote SHA. A branch push is not a merge or deployment.
- Merge, protected-main push, deployment, destructive migration, live payment operation, and physical router change require separate explicit owner authorization.
- CI evidence is necessary but insufficient for product release. Do not merge with open critical security, financial integrity, or wrongful-access failures.
- Shared schema changes require a compatible rollout and recovery plan. Never commit real credentials or customer PII.
