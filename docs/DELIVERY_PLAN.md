# Delivery Plan — vertically sliced

## M0: product and engineering contracts (no code)
M0-01 Residential subscriber lifecycle and state machine; M0-02 money/renewal/refund rules; M0-03 network desired/applied and outage policy; M0-04 roles/RLS matrix; M0-05 data model and migration design; M0-06 UI map and design system; M0-07 mock/lab test strategy. Exit only when contradictions are resolved and acceptance examples exist.

## M1: foundation / first usable vertical slice
Repository scaffold, automated checks, local Supabase, auth/RLS; create a subscriber -> choose service plan -> create installation order -> view order; tests + browser evidence. Then complete site equipment and work order flows.

## M2: payment and entitlement
Invoice -> simulated verified payment -> ledger allocation -> subscription renewal/activation; concurrent event deduplication and cash approval. Keep real money disabled.

## M3: network
Mock provisioning -> offline recovery -> RADIUS -> CHR realistic policy enforcement; status reconciliation; no live network mutations.

## M4: customers and support
Customer portal, hotspot voucher purchase sandbox, ticket intake and technician management.

## M5: operational hardening
Security review, RLS audit, end-to-end 100-user scenarios, outage tests, backup restore, performance checks, runbooks.

## M6: physical acceptance
Conditional on law, upstream contractual permission, hardware and payment provider approval. Pilot with small authorized cohort, verify billing/reconnection and rollback, then progressive rollout.

## Delivery rule
An incomplete vertical slice must not be represented as a complete module. Freeze each contract before agent execution; supersede it by ADR when assumptions change.
