from workflow.workflow_manager import WorkflowManager
from analytics.task_tracker import TaskTracker
from analytics.analytics_engine import AnalyticsEngine
from ui.user_interface import UserInterface

def main():
    workflow_manager = WorkflowManager.get_instance()
    task_tracker = TaskTracker()
    analytics_engine = AnalyticsEngine(task_tracker)
    ui = UserInterface(workflow_manager, analytics_engine, task_tracker)
    ui.run()

if __name__ == "__main__":
    main()
