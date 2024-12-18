from datetime import datetime

class TaskTracker:
    def __init__(self):
        self.current_task = None
        self.start_time = None

    def start_task(self, task_name: str):
        self.current_task = task_name
        self.start_time = datetime.now()

    def end_task(self):
        self.current_task = None
        self.start_time = None

    def get_current_task(self):
        return self.current_task
