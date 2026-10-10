# Community ISP — governed development

**Status:** planning (M0), no physical hardware and no implemented ISP application.

Upload only `chatgpt-project/PROJECT_VISION.md` and `chatgpt-project/PROJECT_PRINCIPLES.md` to ChatGPT Project sources. All live context remains in GitHub. This repository ZIP is a local template, **not evidence of a remote GitHub push**.

First read `AGENTS.md` and `docs/REMOTE_CONTEXT_AND_BRANCH_POLICY.md`.

# Community ISP Management Platform

**Status:** M0 planning, hardware-free. **Target:** 100 subscribers in Cameroon, residential PPPoE and prepaid Wi-Fi hotspot. **Date:** 2026-10-10.

## Product promise
One simple back-office for onboarding, installing, billing, authorizing, renewing, suspending, troubleshooting and supporting customers; a customer self-service portal; and a separately deployed, locally resilient network controller.

## Working rules
- No live commercial activation until upstream resale/contract and local authorization are verified.
- Keep financial truth, service entitlement, desired network state and observed network state separate.
- All features must work in a simulator before real router commissioning.
- No user-facing success claim until the authoritative operation actually succeeds.
- No production deployment, remote database change, secret rotation or network mutation without explicit approval.

## Project documentation
- `PROJECT_BLUEPRINT.md`: original business and module scope.
- `docs/PROJECT_CHARTER.md`: success criteria and non-goals.
- `docs/ENGINEERING_PLAYBOOK.md`: senior-engineering workflow and agent instructions.
- `docs/ARCHITECTURE.md`: system boundaries, deployment and contracts.
- `docs/DELIVERY_PLAN.md`: milestones, vertical slices and quality gates.
- `docs/DECISION_LOG.md` and `docs/adr/`: change-controlled design decisions.
- `docs/contracts/`: behavior contracts to write before implementation.
- `docs/OPEN_QUESTIONS.md`: decisions that must be researched before launch.

## Current next action
M0-01: formalize residential onboarding, payment-to-entitlement, provisioning and renewal state machines including failure paths. Do not scaffold app code until M0 gate is approved.

## Agent entrypoint and drift controls
Before any agent work read [`AGENTS.md`](AGENTS.md), [`docs/PROJECT_STATE.md`](docs/PROJECT_STATE.md), [`docs/CONTEXT_SYNC_PROTOCOL.md`](docs/CONTEXT_SYNC_PROTOCOL.md), and [`docs/tasks/ACTIVE_TASK.md`](docs/tasks/ACTIVE_TASK.md). Run `python3 scripts/verify_project.py`. GitHub CI runs the same governance check. Approval and application tests are separate gates.
