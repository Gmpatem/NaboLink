# NaboLink

NaboLink is a planned ISP management platform for an initial 100 subscribers in Cameroon. **Current stage: M0 planning and governance. No ISP application, deployment, physical hardware, or live payment integration exists.**

The canonical repository is `https://github.com/Gmpatem/NaboLink.git`. `main` is the integration branch; work happens on focused task branches. Read [agent rules](AGENTS.md), [project state](docs/PROJECT_STATE.md), [active task](docs/tasks/ACTIVE_TASK.md), and [remote context policy](docs/REMOTE_CONTEXT_AND_BRANCH_POLICY.md) before development.

The stable [vision](chatgpt-project/PROJECT_VISION.md) and [principles](chatgpt-project/PROJECT_PRINCIPLES.md) hold product intent. Current engineering status, approved decisions, contracts, code, tests, and handoffs live in the repository. The repository copies of the stable documents are not proof of what is currently uploaded to a ChatGPT Project.

The [blueprint](PROJECT_BLUEPRINT.md), [architecture](docs/ARCHITECTURE.md), and [delivery plan](docs/DELIVERY_PLAN.md) describe proposals, not implemented modules. The [subscriber lifecycle contract](docs/contracts/01-subscriber-lifecycle.md) is draft and does not authorize implementation.

Run `python scripts/verify_project.py` for the M0 governance check. It does not test application behavior, legal readiness, payments, or network hardware.
