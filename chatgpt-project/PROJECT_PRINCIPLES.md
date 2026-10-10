# PROJECT PRINCIPLES — Build Boldly, Verify Rigorously

**Version:** 1.0 | **Nature:** Stable engineering culture and decision policy | **Owner approval:** Proposed

## Core philosophy
**Innovate without drifting. Move fast through small, reversible, demonstrably correct increments.** We want the creativity and momentum of AI-assisted development, with the discipline of an experienced engineering team. Governance must reduce rework, not stop experimentation.

## 1. Stable outcome, flexible implementation
Protect the business mission, user needs and approved contracts; actively improve how we satisfy them. A new idea is welcome, but it must explain the customer/operator benefit, tradeoffs, compatibility and test plan. Do not silently replace an agreed workflow, framework or domain contract.

## 2. Contract-first where errors matter
Define state machines, transitions, permissions, financial invariants, network desired/actual states, APIs, migration effects and failure cases before high-risk implementation. Lightweight discovery spikes, UI prototypes and technical experiments **may** happen before approval, but must remain clearly isolated, nonproduction and not falsely presented as implemented product functionality.

## 3. Vertical slices, not disconnected features
Finish a small user journey across interface, domain logic, persistence, authorization and test evidence. Avoid five parallel partly complete dashboards. Keep each slice demoable and reversible.

## 4. Modular monolith first
Prefer a small, comprehensible Next.js/TypeScript + PostgreSQL/Supabase application with clear domains, and a separate local network agent where offline operation requires it. Adopt new infrastructure only for a demonstrated requirement. The real network interface must be replaceable using adapters; simulator and physical implementations must share contracts.

## 5. Trust boundaries and money integrity
Authentication isn't authorization. Verify identity and privileges on server and database boundaries. Prevent cross-customer access. Keep payment records, invoices, entitlements, desired provisioning, applied provisioning and observed session state separate. Make money and provisioning operations idempotent and auditable. Never invent a verified payment or successful activation.

## 6. Failure is a normal workflow
Plan for payment callbacks arriving twice/out of order; slow/unavailable providers; router disconnects; unstable electricity; intermittent cloud access; abandoned installations; expired plans; partial operations; human mistakes. Design retry, reconciliation, human intervention, safe defaults, backups and operational alerts.

## 7. Remote-first, local resilience
The owner operates remotely. The local controller should safely preserve authorized network behavior when the cloud is unreachable and reconcile once connected. Do not put router management credentials in browser code or expose control ports to the internet. Physical commissioning must verify network policies and security, not assume a simulator proved them.

## 8. Simplicity is an engineering requirement
Design for a nontechnical operator. Favor clear statuses, fewer clicks, consistent terminology and actionable errors. Any feature that adds complexity must pay for itself through an observable improvement. Do not bury core workflows under enterprise configuration.

## 9. Evidence, not confidence
Track claims as **proposed / implemented / simulated / tested / remotely pushed / merged / deployed / physically verified**. Run targeted tests and relevant integration, browser and security checks. Tests passing in one layer do not prove full operations; label missing verification explicitly. A task is complete only according to its written acceptance criteria.

## 10. One canonical GitHub source of truth
ChatGPT Project sources hold stable mission and principles, not live work status. For current development questions, fetch the relevant remote branch and SHA, then read its AGENTS.md, project state, active task, approved contracts, decisions and latest handoff. If access is unavailable, say the current remote state cannot be verified. Never use stale chat summaries as authority over remote code.

## 11. Feature branch checkpoint discipline
On approved tasks, agents may commit and push to the **designated nonprotected feature branch** at meaningful checkpoints without asking again for each push. First verify work, document factual state and blockers, commit and push, then confirm the actual remote SHA. WIP checkpoints may push with explicit WIP labeling and disclosed failed tests. **Push is not merge.** Merges, release tagging, production deployment, destructive migrations, live payments and real router changes need separate specific authorization. Never force push shared branches without permission.

## 12. Tight context synchronization
On start: inspect remote branch HEAD, working tree, recent commits, AGENTS.md, ACTIVE_TASK.md, PROJECT_STATE.md, relevant ADRs/contracts, code and tests. On handoff: update state and latest handoff with branch, SHA (or clearly mark pending), files changed, validation commands/results, untested risks, open decisions and next authorized step. Avoid circular claims: post-push confirmation of remote SHA may be in the chat/handoff follow-up rather than falsifying a SHA before commit creation.

## 13. Approved decisions have owners
Make decisions visible as accepted ADRs with alternatives and consequences. To change one, propose an amendment/superseding ADR and migration strategy. Do not let an agent re-interpret a draft as approval. Innovation proposals must be easy to submit and quick to evaluate.

## 14. Keep work reviewable
Small branches, narrow tasks, informative commit messages, clean diffs, minimal coupling and no incidental refactors. Parallel agents should work on nonoverlapping scopes or use planned integration contracts. Resolve conflicts against actual repository state, not remembered intent.

## 15. Operational and regulatory reality
Service resale rights, local permissions, reliable power, available bandwidth, payment providers, geography and customer-router capabilities are unverified until evidenced. Simulations never substitute for licenses or physical tests. Never commit customer secrets, router credentials, personal data or payment tokens.

## 16. Continuous improvement loop
For each completed milestone: review what worked, where agents drifted, test coverage gaps, UI friction and deployment pain. Improve templates/checks only when they clearly reduce mistakes. Reserve explicit room in the roadmap for experiments and usability refinements rather than treating every deviation as failure.

## Priority order when tradeoffs conflict
1. Legal/commercial authorization and user safety
2. Data integrity, security and recoverability
3. Correct business behavior and reliable service
4. Usability and operational clarity
5. Delivery speed and cost
6. Novelty and polish

**Innovation is encouraged within these boundaries, not prohibited by them.**
