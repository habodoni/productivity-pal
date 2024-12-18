class AnalyticsEngine:
    def __init__(self, task_tracker):
        self.task_tracker = task_tracker
        self.productivity_data = []

    def analyze_productivity(self) -> str:
        current_task = self.task_tracker.get_current_task()
        if current_task:
            return f"Currently working on: {current_task}"
        return "No active task"
