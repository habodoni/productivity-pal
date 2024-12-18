class NotificationService:
    def __init__(self):
        self.enabled = True

    def notify(self, message: str):
        if self.enabled:
            print(f"Notification: {message}")

    def toggle(self):
        self.enabled = not self.enabled
        return "Notifications " + ("enabled" if self.enabled else "disabled")
