class NotificationService:
    def __init__(self):
        self.notifications_enabled = True

    def configure_notifications(self, enable):
        self.notifications_enabled = enable
        return "Notifications " + ("enabled" if enable else "disabled")
