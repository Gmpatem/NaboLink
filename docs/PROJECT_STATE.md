# Canonical Project State

Updated: 2026-10-10
Stage: **M0 — Planning / contract definition**
Implementation: **Not started**
Hardware: **None purchased**
Git remote: **Not configured**
Deployment: **None**
Current approved activity: **Establish planning governance and document requirements. No application scaffolding.**

## Confirmed direction
- Build before buying equipment; mock -> CHR/RADIUS lab -> physical commissioning.
- Support residential subscribers and public Wi-Fi vouchers, with distinct policies.
- Initial target 100 subscribers in Cameroon; start single-site, ID model permits expansion.
- Build a simple remotely manageable owner/staff portal plus customer self-service.
- Financial truth, subscription entitlement, desired/applied access and observed connectivity are separate.

## Proposed, not yet approved
- Exact stack/runtime choices beyond the existing preliminary architecture.
- Service-specific SLA, grace periods, plan speeds/device limits and MoMo provider.
- Payment reconciliation policy, local outage authorization limits and router setup strategy.
- Detailed role permissions, complete schema and state transition tables.

## Current milestone and gate
M0: write and review contracts for subscriber lifecycle, billing/ledger, network provisioning, authorization/RLS, database invariants, UI flows and test fixtures.
**M0 gate is NOT passed.** No application feature is certified or implemented.

## Next action
Finish `docs/contracts/01-subscriber-lifecycle.md` including edge cases and acceptance examples; request explicit owner approval before moving to implementation.

## Context maintenance
Change this file at each approved handoff: date, milestone, what is verified, current branch/SHA, outstanding blockers, exact next task. Do not claim remote deployment or real hardware tests.
