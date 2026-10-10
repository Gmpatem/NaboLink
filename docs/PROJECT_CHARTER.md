# Project Charter — v0.1

## Users
Owner (remote), local operator, technician, residential subscriber, public hotspot user, automation.

## Primary outcomes
- Register a customer once, create multiple independently billed services.
- Issue auditable invoices; verified payments extend entitlement exactly once.
- Provision internet authorization with explicit pending/applied/failed states.
- Preserve pre-existing authorized service during cloud interruption according to configurable bounded local policy.
- Offer a minimal self-service customer portal and technician work queue.
- Report finance and network health without inventing live data.

## V1 boundaries
In: single site with multi-site-ready keys; residential PPPoE; public hotspot vouchers; prepaid billing; mobile-money sandbox plus audited cash; RADIUS; virtual RouterOS; support tickets; operator roles.
Out: native mobile apps, payroll, complex CRM, customer data resale, bandwidth guarantees not tested against upstream service, advanced forecasting, uncontrolled automation.

## Success criteria
Demonstrate at least 100 synthetic subscribers; no cross-role data access; duplicate payment callbacks never double-credit; pending router commands are not shown as applied; cloud outage and recovery reconcile correctly; operator can complete enrollment-to-active in a guided workflow.

## Launch gate
Regulatory/commercial authorization, hardware commissioning, real payment gateway approval, on-site coverage and power resilience testing must all pass before accepting paying customers.
