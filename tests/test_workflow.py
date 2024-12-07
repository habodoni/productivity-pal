import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from workflow_management.workflow_manager import WorkflowManager

class TestWorkflowManager(unittest.TestCase):
    def setUp(self):
        # Reset the singleton instance before each test (optional for isolation)
        WorkflowManager._instance = None

    def test_switch_mode_valid(self):
        wm = WorkflowManager.get_instance()  # Use Singleton method
        result = wm.switch_mode("focus")
        self.assertIn("Switched to focus mode", result)

    def test_switch_mode_invalid(self):
        wm = WorkflowManager.get_instance()  # Use Singleton method
        result = wm.switch_mode("invalid")
        self.assertIn("Invalid mode", result)

if __name__ == "__main__":
    unittest.main()
