# Architecture — preliminary v0.1

## Decision
Modular monolith for web/backend; independently deployed site agent and RADIUS for local access decisions; durable job runner for async work. Single repository (pnpm workspace) with separated packages and runtimes; do not deploy the network worker as a Vercel request handler.

## Proposed future repository layout
```
apps/web/                 # Next.js: owner/staff/customer UI + server API
apps/worker/              # durable billing, outbox and reconciliation jobs
apps/site-agent/          # secure on-site Linux controller, outbound connectivity
packages/domain/          # types, money, entitlements, state transitions
packages/contracts/       # shared validated commands/events and schema versions
packages/network-adapters/# mock adapter + RouterOS adapter
packages/ui/              # UI components and design system
supabase/migrations/      # versioned database changes
supabase/tests/           # RLS and DB invariant tests
tests/e2e/                # Playwright scenarios
tests/lab/                # CHR/RADIUS/network fault scenarios
docs/adr/                # architectural decision records
```

## Modules
Identity/RBAC; Customers; Sites/Equipment; Catalog/Plans; Orders/Installation; Subscriptions/Entitlements; Invoices/Payments/Ledger; Network/Provisioning; Hotspot; Support; Notifications; Reporting/Audit.

## Authority boundaries
Payment providers and audited cash handling -> verified payment events. Billing ledger -> financial truth. Entitlement engine -> time-bounded authorization. Provisioning outbox -> desired access. Site agent/RADIUS/RouterOS -> applied state and observed sessions. UI only reflects authoritative state with timestamps.

## Network security
Never expose management ports to public internet; server-issued commands authenticated and authorized; site agent maintains outbound secure channel; short-lived service credentials and secret rotation; site private LAN to RouterOS and RADIUS. Offline authorization bounds and expired policy handling defined before launch.

## Development environments
local mock -> virtual lab with MikroTik CHR + RADIUS -> staging with isolated keys and generated accounts -> approved physical pilot -> production. No real customer data in simulator.

## Mandatory fault scenarios
Webhook duplicate/delayed; payment succeeds and router offline; agent crashes mid-command; cloud lost for hours; local power interruption; stale entitlement; two operators register same customer; two payments race; CHR refuses policy; partial install; reverse payment after access granted; RADIUS auth failure.
