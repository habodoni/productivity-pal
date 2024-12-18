class Mode:
    def __init__(self, name: str, app_manager):
        self.name = name
        self.app_manager = app_manager
        self._configure_apps()

    def _configure_apps(self):
        if self.name == "focus":
            self.app_manager.set_apps(["Notion", "Slack"])
        elif self.name == "meeting":
            self.app_manager.set_apps(["Zoom", "Outlook"])
