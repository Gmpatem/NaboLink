# NaboLink — Project Blueprint v0.1
Date: 2026-10-10
Status: Planning / hardware-free
Market: Cameroon; initial 100 subscribers

## Product goal
A simple owner-controlled ISP management system for residential PPPoE internet and prepaid public Wi-Fi, built and validated virtually before physical hardware is purchased. Customer, money and network state must never be conflated.

## Guardrails
- No live reseller activation until provider and local regulatory permissions are confirmed.
- Hardware-independent architecture, upstream provider not hardcoded to Starlink.
- Remote administration; no public router management ports.
- Access enforcement local-first with clear outage behavior.
- Payment is only marked paid after verified server-side evidence or authorized audited cash receipt.
- Visible desired network state versus confirmed actual state.
- Functional operations before advanced analytics or cosmetics.

## People and permissions
Owner: global operations, plans, refunds, access overrides, finances, network approval and settings.
Operator: onboard customers, invoices, payments subject to authorization, support triage.
Technician: assigned installations, equipment, work orders, troubleshooting; no customer finance administration.
Customer: own service, invoices, renewals, receipts, tickets.
Automation: idempotent scheduled billing, expiry, notifications, provisioning and reconciliation.

## Service products
1. Residential: ongoing subscription, PPPoE credentials, customer equipment, monthly billing.
2. Hotspot: prepaid entitlement with voucher/captive portal, session/device/time policies.
Distinct policies and activation paths, shared CRM, payments, network sites and reporting.

## Core workflows and success criteria
### Residential onboarding
Create customer and address -> choose plan -> create service order -> site feasibility/install -> invoice -> verified payment -> ready-to-activate -> request access provisioning -> device confirms configured -> active. Guard duplicate customers, failed installations, unverified payments and pending network jobs.
### Renewal
Generate invoice before expiry -> reminder -> payment attempt -> payment provider webhook verification and deduplication -> ledger allocation -> extend paid-through date -> sync policy -> receipt. Handle failed/partial/overpayments and delayed provider callbacks.
### Expiry/suspension
Scheduled evaluate entitlement and grace -> desired access denied -> local controller applies or queues -> network reports result -> customer notified. Manual exceptions require scope, reason, actor and expiration.
### Public hotspot
Choose voucher plan -> payment verified -> issue unique voucher -> captive portal login -> authorize RADIUS -> enforce duration/device/speed limits -> accounting/expiry -> revoke.
### Support and repair
Ticket -> diagnostics (billing/account/router/site) -> classify outage versus user problem -> assignment -> resolution -> customer confirmation.
### Equipment and installation
Receive stock -> assign device to job -> install with serial/MAC and photos -> acceptance tests -> commissioned or returned; inventory traceable.
### Daily closing
View verified payment ledger, cash receipts, reversals, unpaid invoices, active subscriber totals, unresolved faults and technician jobs. Audit all manual adjustments.
### Cloud/network outage
Existing local authorized sessions continue according to cached bounded entitlements; new activations and revocations queue safely; sync resumes and reconciles on reconnect. Never label queued actions applied.

## V1 module map
Owner overview; Subscribers; Services/Subscriptions; Plans; Billing/Payments; Network Sites; Provisioning/Devices; Installations/Tickets; Hotspot/Vouchers; Reports; Staff/Settings; Customer portal.

## Recommended architecture
Web: Next.js TypeScript Tailwind shadcn/ui.
Backend: Postgres (Supabase possible), RLS, server-side command APIs and durable queue/outbox, background worker.
Local: Linux site agent, RouterOS connector, FreeRADIUS (or evaluated equivalent), local policy cache and operational logs.
Virtual lab: mock RouterOS adapter, FreeRADIUS integration, MikroTik CHR VM, fake payment provider and synthetic clients.
Networking: secure outbound tunnel/agent authentication, router management restricted to private network. No browser-to-router calls.
Deploy: web Vercel; jobs and network control on appropriate always-on worker/agent infrastructure.

## Core entities
organizations, sites, staff_memberships, role_grants, customers, customer_addresses, service_orders, installation_jobs, plans, plan_versions, subscriptions, service_entitlements, invoices, invoice_lines, payment_attempts, payments, payment_allocations, refunds, ledger_entries, network_devices, equipment_inventory, device_assignments, network_accounts, desired_network_policies, provisioning_commands, provisioning_results, network_sessions, usage_summaries, hotspot_vouchers, support_tickets, notifications, audit_events, system_settings.
Key constraints: customer may have many services; invoice/payment is not service activation; network desired/applied status explicit; gateway events idempotent; unique active vouchers and router accounts, scoped to site/organization.

## Service states
Service order: draft -> awaiting_installation -> awaiting_payment -> ready_to_provision -> provisioning -> fulfilled (or cancelled/failed).
Subscription: pending -> active -> grace -> expired/suspended -> cancelled; keep reason history.
Provisioning: pending -> executing -> applied, or retryable_failure/permanent_failure.
Invoice: draft -> issued -> partly_paid/paid/void/overdue.
Payment: initiated -> pending -> verified/failed/refunded; use separate refund records.
Hotspot voucher: issued -> active -> exhausted/expired/revoked.

## Initial price assumptions (NOT approved commercial tariffs)
Basic 2,500 XAF/month; Home 4,000 XAF/month; Pro 7,000 XAF/month; Business 12,000–20,000 XAF/month. Speeds, contention, data caps, device limits, grace period, installation charges and hotspot rates remain undecided, must be configurable.

## Build milestones and acceptance gates
M0 Project contracts and diagrams: scope, permission matrix, data glossary, state machines, exceptional flows, decision log.
M1 Usable CRM: staff auth, customers, plans, orders, subscriptions, install tickets; complete with seed demo data and tests.
M2 Financial control: invoices, mock wallet, cash approvals, payment reconciliation, receipts and renewal engine; no double credit under webhook retries.
M3 Virtual network: adapter contract, mock agent, CHR and RADIUS lab, provisioning state reconciliation, PPPoE and hotspot authentication verification.
M4 Customer portal, voucher purchase and service desk, notification templates.
M5 Security and resilience: RLS matrix, rotation, site outage tests, backup restore, alarms and 100+ subscriber scenarios.
M6 Physical pilot: after authorizations and hardware; router commissioning, real payment credentials, coverage, power, monitoring and rollback tests.

## Open decisions to resolve in design
- Intended launch area and service topology (residential cable/wireless distribution and hotspot sites).
- Whether home CPE supports PPPoE natively and installation standards.
- Commercial speeds/limits; upstream bandwidth and fair-use model; no false guarantees.
- Exact payment aggregator/merchant registration; cash handling and refunds.
- Offline expiry behavior and how long cached authorization remains valid.
- Ownership and location of on-site always-on controller and power backup.
- Starlink resale permission and Cameroon ART licensing category.
- Deployment accounts and product branding details.

## Planning sequence
M0 contracts and acceptance scenarios remain to be drafted and approved. `docs/tasks/ACTIVE_TASK.md` records the current authorized task; this blueprint does not authorize M1 implementation.
