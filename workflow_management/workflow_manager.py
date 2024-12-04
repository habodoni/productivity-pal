class WorkflowManager:
    def __init__(self):
        self.modes = {"focus": ["Notion", "Slack"], "meeting": ["Zoom", "Outlook"]}
        self.current_mode = None

    def switch_mode(self, mode):
        if mode in self.modes:
            self.current_mode = mode
            return f"Switched to {mode} mode with apps: {', '.join(self.modes[mode])}"
        else:
            return "Invalid mode. Available modes: " + ", ".join(self.modes.keys())
