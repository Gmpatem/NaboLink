#!/usr/bin/env python3
"""Check objective M0 repository governance facts; not product readiness."""

from pathlib import Path
import re
import subprocess
import sys

from governance_context import context_errors

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "Gmpatem/NaboLink"
REQUIRED = (
    "AGENTS.md",
    "README.md",
    "chatgpt-project/PROJECT_VISION.md",
    "chatgpt-project/PROJECT_PRINCIPLES.md",
    "docs/REMOTE_CONTEXT_AND_BRANCH_POLICY.md",
    "docs/BRANCH_AND_RELEASE_POLICY.md",
    "docs/PROJECT_STATE.md",
    "docs/tasks/ACTIVE_TASK.md",
    "docs/DECISION_LOG.md",
    "docs/handoffs/LATEST.md",
    "docs/templates/HANDOFF_TEMPLATE.md",
    "docs/contracts/01-subscriber-lifecycle.md",
    ".github/workflows/governance.yml",
)
IDENTITY_FILES = (
    "AGENTS.md",
    "README.md",
    "chatgpt-project/PROJECT_INSTRUCTIONS_TO_PASTE.md",
    "docs/REMOTE_CONTEXT_AND_BRANCH_POLICY.md",
    "docs/PROJECT_STATE.md",
    "docs/handoffs/LATEST.md",
)
HANDOFF_FIELDS = (
    "Repository", "Feature branch", "Base branch", "Starting SHA",
    "Latest known local SHA", "Push result and remote SHA", "Milestone",
    "Active task", "Approved scope", "Changed files", "Verification results",
    "Known failures", "Incomplete items", "Pending decisions",
    "Contract impact", "Next authorized step",
)
errors: list[str] = []


def read(path: str) -> str:
    file = ROOT / path
    if not file.is_file():
        errors.append(f"Missing: {path}")
        return ""
    data = file.read_text(encoding="utf-8")
    if not data.strip():
        errors.append(f"Empty: {path}")
    return data


for path in REQUIRED:
    read(path)

for path in IDENTITY_FILES:
    data = read(path)
    if REPOSITORY not in data:
        errors.append(f"Canonical repository missing: {path}")
    if re.search(r"Community ISP", data, re.IGNORECASE):
        errors.append(f"Obsolete project identity: {path}")
    for match in re.finditer(r"github\.com/([\w.-]+/[\w.-]+)", data):
        if match.group(1).removesuffix(".git") != REPOSITORY:
            errors.append(f"Unexpected GitHub repository in {path}")

state = read("docs/PROJECT_STATE.md")
active = read("docs/tasks/ACTIVE_TASK.md")
handoff = read("docs/handoffs/LATEST.md")
template = read("docs/templates/HANDOFF_TEMPLATE.md")
contract = read("docs/contracts/01-subscriber-lifecycle.md")

errors.extend(context_errors(state, active, handoff))
milestone = re.search(r"(?m)^Stage:\s*\*\*(M\d+)\b", state)
if milestone and milestone.group(1) == "M0" and "Implementation: **Not started**" not in state:
    errors.append("M0 project state must state implementation is not started")
if not re.search(r"(?m)^Status:\s*\*\*(?:DRAFT|APPROVED|SUPERSEDED)\b", contract):
    errors.append("Subscriber contract lacks explicit approval status")
for path, data in (("latest handoff", handoff), ("handoff template", template)):
    for field in HANDOFF_FIELDS:
        if not re.search(rf"(?m)^{re.escape(field)}:", data):
            errors.append(f"{path} missing field: {field}")

for file in (ROOT / "docs/adr").glob("*.md"):
    if file.name != "README.md" and not re.search(
        r"(?m)^Status:\s*(?:Proposed|Accepted|Superseded)\b",
        file.read_text(encoding="utf-8"),
    ):
        errors.append(f"ADR missing status: {file.relative_to(ROOT)}")

for path in ("apps", "packages", "supabase/migrations"):
    if milestone and milestone.group(1) == "M0" and (ROOT / path).exists():
        errors.append(f"Application path exists during M0: {path}")

tracked = subprocess.run(
    ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=False,
)
if tracked.returncode:
    errors.append("Could not inspect Git index for committed secrets")
else:
    secret_patterns = (
        re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
        re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
        re.compile(r"sk-[A-Za-z0-9]{24,}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    )
    for raw in tracked.stdout.split(b"\0"):
        if not raw:
            continue
        path = Path(raw.decode("utf-8"))
        if path.name == ".env" or path.name.startswith(".env.") and path.name != ".env.example":
            errors.append(f"Tracked environment file: {path}")
        file = ROOT / path
        if not file.is_file() or path.as_posix() == "scripts/verify_project.py":
            continue
        data = file.read_text(encoding="utf-8", errors="ignore")
        if any(pattern.search(data) for pattern in secret_patterns):
            errors.append(f"Possible credential in tracked file: {path}")

if errors:
    print("FAIL governance checks:")
    for error in sorted(set(errors)):
        print(f" - {error}")
    sys.exit(1)
print(f"PASS governance checks ({len(REQUIRED)} required files, identity, status, handoff, obvious-secret scan)")
print("No application, legal, deployment, payment, or physical network validation was performed.")
