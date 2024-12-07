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
        self.modes = {"focus": ["Notion", "Slack"], "meeting": ["Zoom", "Outlook"]}
        self.current_mode = None

    def switch_mode(self, mode):
        if mode in self.modes:
            self.current_mode = mode
            return f"Switched to {mode} mode with apps: {', '.join(self.modes[mode])}"
        else:
            return "Invalid mode. Available modes: " + ", ".join(self.modes.keys())
