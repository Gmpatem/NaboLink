# CONTRACT-001 — Subscriber lifecycle

Status: **DRAFT — NOT APPROVED**
Owner approval: Pending
Implementation authorized: No

## In scope
Residential registration, quote/plan selection, installation, invoice, verified payment, entitlement, provisioning, expiry, suspension and renewal. Public Wi-Fi access is a separate contract.

## Required invariants
- Creating a customer alone never enables network service.
- A paid invoice alone never implies physical connectivity.
- Only verified payments contribute to prepaid entitlement unless a separately authorized, audited credit policy exists.
- A request for provisioning is not proof of applied access.
- Retries are idempotent. Payment provider event IDs must be unique within provider and merchant scope.
- Staff cannot silently override payments, entitlement or access.
- Every state transition records who/what caused it, when, why and correlation ID.

## Questions for owner sign-off
1. Exact prepaid cycle: calendar month vs 30 days vs configurable term?
2. Does paid subscription time start upon completed installation or upon payment?
3. Are grace periods allowed; who approves and for how long?
4. Installation fees and refundable/non-refundable rules?
5. Can one customer have multiple separately billed connections?
6. Does renewal stack from current expiry if early, or reset from payment time?
7. What happens to paid customers during extended site power outage?

## Acceptance scenarios to formalize
- New customer registered without plan or payment: no access.
- Payment verified before technician completes installation: pending activation, never falsely online.
- Verified payment delivered twice: one allocation and one entitlement transition.
- Agent offline during activation: authorized entitlement stays valid and provisioning remains pending/retryable.
- Invoice becomes overdue: no suspension unless applicable entitlement has actually expired.
- Renewal and expiry jobs race: deterministic result, no wrongful suspension.
- Failed physical provisioning: alert operator with recoverable attempt history.

**No code until contract status is APPROVED.**
