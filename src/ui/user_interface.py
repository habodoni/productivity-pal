from workflow.workflow_manager import WorkflowManager
from analytics.analytics_engine import AnalyticsEngine
from analytics.task_tracker import TaskTracker

class UserInterface:
    def __init__(self, workflow_manager, analytics_engine, task_tracker):
        self.workflow_manager = workflow_manager
        self.analytics_engine = analytics_engine
        self.task_tracker = task_tracker

    def display_menu(self):
        print("\n=== Productivity Pal ===")
        print("Available commands:")
        print("- focus         : Switch to focus mode")
        print("- meeting       : Switch to meeting mode")
        print("- start task    : Start a new task")
        print("- end task      : End the current task")
        print("- status        : View current task or productivity status")
        print("- exit          : Exit the program")

    def process_command(self, command: str) -> str:
        if command == "focus":
            return self.workflow_manager.switch_mode("focus")
        elif command == "meeting":
            return self.workflow_manager.switch_mode("meeting")
        elif command == "start task":
            task_name = input("Enter task name: ").strip()
            if task_name:
                self.task_tracker.start_task(task_name)
                return f"Started task: {task_name}"
            else:
                return "Task name cannot be empty."
        elif command == "end task":
            self.task_tracker.end_task()
            return "Task ended"
        elif command == "status":
            return self.analytics_engine.analyze_productivity()
        elif command == "exit":
            return "Goodbye!"
        else:
            return "Invalid command. Please try again."

    def run(self):
        while True:
            self.display_menu()
            command = input("\nEnter a command: ").strip().lower()
            response = self.process_command(command)
            print(f"\n{response}")
            if command == "exit":
                break
