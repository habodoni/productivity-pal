import unittest
from workflow_management.workflow_manager import WorkflowManager

class TestWorkflowManager(unittest.TestCase):
    def test_switch_mode_valid(self):
        wm = WorkflowManager()
        result = wm.switch_mode("focus")
        self.assertIn("Switched to focus mode", result)

    def test_switch_mode_invalid(self):
        wm = WorkflowManager()
        result = wm.switch_mode("invalid")
        self.assertIn("Invalid mode", result)

if __name__ == "__main__":
    unittest.main()
