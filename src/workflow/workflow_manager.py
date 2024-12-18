from .application_manager import ApplicationManager
from .mode import Mode
from notifications.notification_service import NotificationService

class WorkflowManager:
    _instance = None

    @staticmethod
    def get_instance():
        if WorkflowManager._instance is None:
            WorkflowManager._instance = WorkflowManager()
        return WorkflowManager._instance

    def __init__(self):
        if WorkflowManager._instance is not None:
            raise Exception("This class is a singleton!")
        self.current_mode = None
        self.app_manager = ApplicationManager()
        self.notification_service = NotificationService()

    def switch_mode(self, mode_name: str) -> str:
        self.current_mode = Mode(mode_name, self.app_manager)
        self.notification_service.notify(f"Switched to {mode_name} mode")
        return f"Switched to {mode_name} mode"
