from ui.ui import UserInterface
from workflow_management.workflow_manager import WorkflowManager
from analytics.analytics_engine import AnalyticsEngine
from notifications.notification_service import NotificationService

if __name__ == "__main__":
    ui = UserInterface()
    wm = WorkflowManager()
    ae = AnalyticsEngine()
    ns = NotificationService()

    while True:
        command = ui.get_user_command()
        if command == "focus mode":
            response = wm.switch_mode("focus")
        elif command == "analyze productivity":
            response = ae.analyze_productivity()
        elif command == "disable notifications":
            response = ns.configure_notifications(False)
        elif command == "exit":
            break
        else:
            response = "Unknown command. Try again."
        ui.display_response(response)
