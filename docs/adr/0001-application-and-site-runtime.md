# ADR-0001 — Core application and site runtime
Status: Proposed
Date: 2026-10-10

## Context
Initial service has ~100 subscribers. Cloud-hosted management must not be a network single point of failure.

## Decision
Modular monolith for core SaaS and a separate local site agent/RADIUS. Workers handle durable async commands. A shared schema version ensures compatibility.

## Consequences
Low cloud app complexity, clear separation of financial and local network reliability. Requires agent protocol, replay/idempotency and site deployment operations.
