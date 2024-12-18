class ApplicationManager:
    def __init__(self):
        self.active_apps = []

    def set_apps(self, apps: list):
        self.active_apps = apps
        for app in apps:
            self.launch_app(app)

    def launch_app(self, app: str):
        print(f"Launching {app}")
