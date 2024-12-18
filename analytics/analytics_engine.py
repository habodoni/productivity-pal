class AnalyticsEngine:
    def __init__(self):
        self.data = []

    def log_task(self, task_name, time_spent):
        self.data.append({"task": task_name, "time": time_spent})

    def analyze_productivity(self):
        if not self.data:
            return "No data to analyze."
        total_time = sum(task["time"] for task in self.data)
        return f"Total productivity time logged: {total_time} minutes"

    def generate_detailed_report(self):
        if not self.data:
            return "No data available for detailed analysis."
        task_summary = "\n".join([f"{task['task']}: {task['time']} minutes" for task in self.data])
        total_time = sum(task["time"] for task in self.data)
        return f"Task Summary:\n{task_summary}\nTotal Time Logged: {total_time} minutes"
