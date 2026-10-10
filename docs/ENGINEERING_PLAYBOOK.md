# Engineering Playbook — v0.1

## Delivery method
Contract-first, risk-first, vertical slices using a modular monolith plus separate local controller. Each slice delivers UI + server behavior + persistence + authorization + tests + operator instructions.

## Rules carried forward from CradleHub and the medical blog
1. INSPECT before change: read current charter, contracts, ADRs, code, schema, migration history and branch status.
2. Diagnose the root cause and avoid implementing a second engine for existing functionality.
3. Keep backend authority canonical; never let a frontend label, cached counter or mock claim real success.
4. Use a frozen design system and complete all routed screens; never deliver an unmouted UI prototype as a completed application.
5. Separate pure planning, local coding, staging deployment, production migration and live network changes into independently approved actions.
6. Keep changes focused and reversible. Do not rewrite unrelated modules.
7. Capture reproducible evidence and label it correctly: typecheck != browser test != network integration test.
8. Automate normal operations with scoped, expiring, reasoned, audited authorized manual overrides.
9. Keep a decision log and current handoff for every coding-agent session.
10. Stop on P0 security, money-integrity, or network-access blockers. Do not misrepresent a partial pass as release-ready.

## Branch and change discipline
- Protected `main`; short-lived `feat/*`, `fix/*`, `docs/*`; review before merge.
- One issue / one vertical slice / one PR when practical.
- Schema migrations forward-only once shared; include compatible rollout and rollback/compensation plans.
- Exact source commit and migration version recorded in deployment evidence.
- Avoid simultaneous agents writing the same files; parallelize research, tests, or isolated components instead.

## Agent task contract
Every agent instruction includes: objective, in-scope/out-of-scope paths, existing design/contracts, required interfaces, data/permission rules, allowed actions, tests, acceptance criteria, stopping conditions, evidence format.
Required response: starting SHA, branch, files touched, behavior diff, migration diff, tests actually run, untested paths, risks, recommended next step.

## Quality gates
- G0 Contract: product rules, boundaries, failure modes, acceptance tests approved.
- G1 Local: formatting, lint, typecheck, unit tests, database/RLS tests, test build pass.
- G2 Integrated: API and UI browser tests with real database; payment retry/concurrency; virtual agent and RADIUS tests.
- G3 Staging: secrets scan, negative auth tests, observability, restore drill, failure simulation, 100-subscriber scenarios.
- G4 Physical: CHR parity audit, actual device integration, equipment tests, regulatory approval and explicit owner go-live signoff.

## Definition of done
Working user flow, authoritative backend, permission matrix, repeatable migration, failure handling, useful logs, tests at relevant layers, accessibility/responsive check, docs and proof. Mock work must always be visibly marked mock.
