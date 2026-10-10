# Branch and Release Policy
- Protect `main` on GitHub after remote creation. Require PR reviews and passing CI. Disable direct pushes where supported.
- Tasks use `docs/*`, `feat/*`, `fix/*`, `test/*`; do not mix unrelated refactors.
- CI checks are necessary, never sufficient; approvals remain human-driven.
- Production deploy, payment gateway activation, database migration, live router changes and actual subscription enforcement are separate explicit approvals.
- No real credentials or personally identifying customer fixtures in repo.
- Do not merge when P0 security, financial integrity or wrong-access failure is open.
- Require backward-compatible DB migrations and an operational recovery plan.
