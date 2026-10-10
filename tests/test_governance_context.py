import unittest

from scripts.governance_context import active_task_id, context_errors


STATE = "Stage: **M0 — Planning**\nWorking branch: `chore/m0-governance-initialization`\nActive task: M0-A corrective checkpoint\n"
ACTIVE = "# Active Task — M0-A corrective checkpoint\nMilestone: M0\nBranch: `chore/m0-governance-initialization`\n"
HANDOFF = "Milestone: M0 governance\nActive task: M0-A corrective checkpoint\nFeature branch: `chore/m0-governance-initialization`\n"


class GovernanceContextTests(unittest.TestCase):
    def test_supported_ids(self):
        for task_id in ("GOV-002", "M0-A", "M0-01"):
            with self.subTest(task_id=task_id):
                self.assertEqual(active_task_id(f"# Active Task — {task_id} work\n"), task_id)

    def test_malformed_ids(self):
        for task_id in ("GOV-2", "GOV-ABC", "M0-AA", "M0-1", "m0-A", "M0-A1", "M0-A/extra"):
            with self.subTest(task_id=task_id):
                self.assertIsNone(active_task_id(f"# Active Task — {task_id} work\n"))

    def test_consistent_context(self):
        self.assertEqual(context_errors(STATE, ACTIVE, HANDOFF), [])

    def test_detects_task_milestone_and_branch_drift(self):
        self.assertIn("Handoff active task differs from active task file", context_errors(STATE, ACTIVE, HANDOFF.replace("M0-A", "M0-01")))
        self.assertIn("Active task milestone differs from project state", context_errors(STATE, ACTIVE.replace("Milestone: M0", "Milestone: M1"), HANDOFF))
        self.assertIn("Project state branch differs from active task", context_errors(STATE.replace("chore/m0-governance-initialization", "docs/other"), ACTIVE, HANDOFF))


if __name__ == "__main__":
    unittest.main()
