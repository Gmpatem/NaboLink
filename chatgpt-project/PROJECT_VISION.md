# PROJECT VISION — NaboLink Cameroon

**Version:** 1.0 | **Nature:** Stable product intent, not a development status report | **Owner approval:** Proposed

## Why we are building this
Build a trustworthy, easy-to-operate internet service business platform for communities in Cameroon, starting with one service area and approximately **100 paying subscribers**. Internet access can create opportunities for education, remote work, small businesses, families and community services. Our software should help a small local team provide and sustain that access without requiring deep networking knowledge.

The business is intended to start with an authorized upstream internet connection (potentially Starlink), a MikroTik-managed local network, household service subscriptions, and optional public Wi-Fi hotspots. No equipment has been purchased; all physical assumptions remain provisional. Build and test virtually first. Launch only after applicable supplier terms, permissions and local regulatory requirements are verified.

## Intended customers and users
- **Residential subscriber:** wants predictable, affordable monthly access, clear prices, convenient renewals and prompt help.
- **Hotspot customer:** wants understandable voucher pricing, fast login and fair time/device limits.
- **Local operator:** needs to register customers, see payment/service status, resolve common issues and escalate exceptions with minimal clicks.
- **Technician:** needs concise installation tasks, equipment assignment, test instructions and traceable fault tickets.
- **Remote owner:** needs accurate cash position, service health, operational oversight and alerts, without having to operate the router manually every day.

## Product promise
One simple platform to onboard subscribers; price and provision service; issue invoices; verify payments; renew, suspend and restore entitlements; manage hotspot access; surface equipment/network faults; and support customers. **Never describe internet as activated until access has actually been provisioned and checked.**

## Business objectives
1. Operate an initial single-site network for roughly 100 subscribers with a small team and remote oversight; grow based on verified demand and capacity.
2. Reduce missed payments, manual bookkeeping, ambiguous renewals and support friction.
3. Give customers transparent service terms, accurate receipts, clear expiry information and a path to support.
4. Keep costs proportional to scale; prioritize uptime, recoverability and security over expensive complexity.
5. Keep account history, tariff history, payment history and provisioning decisions auditable.
6. Preserve the option to grow into additional neighborhoods, access points, upstream providers and sites without changing the business core.

## Commercial starting assumptions — NOT approved tariffs
Legacy discussion suggested Basic 2,500 FCFA, Home 4,000 FCFA, Pro 7,000 FCFA, Business 12,000–20,000 FCFA monthly. Speeds, device limits, capacity, costs, fairness policies, payment fees and final prices must be modeled and reviewed; no guarantee or plan advertised before testing. Upstream price and reseller eligibility are not verified.

## Two intentionally distinct service models
**Residential:** customer + address + installation + one or more subscriptions + monthly prepaid entitlement, provisioned using a tested supported access method (PPPoE proposed). Lifecycle includes signup, installation, verification, activation, renewal, grace handling, expiration, cancellation and reconnection.

**Public Wi-Fi:** prepaid voucher or session with captive portal, time/device/speed policy and verified payment; not forced into the same installation or billing flow as residential. Can be staged behind residential MVP if justified.

## User experience aspirations
- One operational homepage with the few highest-value actions and exceptions.
- Plain-language states: paid, pending, provisioning, online observed, expired, suspended, failed; never collapse them into one misleading 'active' label.
- Mobile-first customer access, usable on low-cost phones and limited networks.
- Efficient local workflows: minimal navigation, robust search, accessible errors and recovery actions.
- English-first implementation with internationalization-ready copy; other languages chosen by actual customer demand.

## What success looks like
A trained operator can onboard, bill, renew and support a customer without editing router commands; a customer can pay and understand the resulting access state; a remote owner can reconcile money and service; cloud outages do not unnecessarily cut off existing authorized access; a virtual 100-subscriber trial can run without reconciliation failures; and a real pilot can be commissioned through a documented checklist.

## Explicit non-goals for the first release
No giant telecom ERP, no dedicated native mobile apps, no speculative AI features, no microservice constellation, no unsupported real-time traffic claims, no automatic financial or network mutations without a testable contract. Building a capable platform is more important than building many screens.

## Innovation mandate
**We should invent and improve deliberately.** Propose useful automation, better service experiences, smarter diagnostics and lower-cost network controls whenever they solve real customer or operator problems. Evaluate innovations in short experiments or separate feature branches with success metrics, cost, security and rollback plans. Celebrate evidence-backed improvements; avoid feature accumulation just because a capability is technically possible. Architecture should create room to experiment, not become an excuse to refuse creative ideas.

## Long-term direction
Expand after product-market and operational validation: multiple coverage areas, technician operations, site-level reporting, alternative upstream providers, device inventory, network health trends, and optionally fair-use and performance analytics. Expansion is a choice informed by real operating evidence, not a commitment to build everything now.

## Boundaries
This document governs **why and for whom** the system exists. Actual features, decisions, implementation status, branch SHAs and releases are tracked in the GitHub repository, not in these stable ChatGPT Project sources. Update this vision only when the product mission materially changes and the owner approves the change.
