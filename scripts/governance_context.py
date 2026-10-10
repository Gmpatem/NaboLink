"""Small, testable checks for the branch-scoped governance context."""

import re

TASK_ID = re.compile(r"(?:[A-Z]{2,8}-\d{3}|M\d+-(?:[A-Z]|\d{2}))\Z")


def field(text: str, label: str, pattern: str = r"(\S+)") -> str | None:
    match = re.search(rf"(?m)^{re.escape(label)}:\s*{pattern}", text)
    return match.group(1) if match else None


def active_task_id(active: str) -> str | None:
    match = re.search(r"(?m)^# Active Task\s*[—-]\s*(\S+)", active)
    candidate = match.group(1) if match else None
    return candidate if candidate and TASK_ID.fullmatch(candidate) else None


def context_errors(state: str, active: str, handoff: str) -> list[str]:
    errors = []
    milestone = field(state, "Stage", r"\*\*(M\d+)\b")
    task = active_task_id(active)
    branch = field(active, "Branch", r"`([^`]+)`")
    if not milestone:
        errors.append("Project state lacks a parseable milestone")
    if not task:
        errors.append("Active task has a missing or malformed task ID")
    if not branch:
        errors.append("Active task lacks a parseable branch")
    if milestone:
        if field(active, "Milestone", r"(M\d+)\b") != milestone:
            errors.append("Active task milestone differs from project state")
        if field(handoff, "Milestone", r"(M\d+)\b") != milestone:
            errors.append("Handoff milestone differs from project state")
    if task:
        for name, data in (("Project state", state), ("Handoff", handoff)):
            if field(data, "Active task") != task:
                errors.append(f"{name} active task differs from active task file")
    if branch:
        if field(state, "Working branch", r"`([^`]+)`") != branch:
            errors.append("Project state branch differs from active task")
        if field(handoff, "Feature branch", r"`([^`]+)`") != branch:
            errors.append("Handoff branch differs from active task")
    return errors
