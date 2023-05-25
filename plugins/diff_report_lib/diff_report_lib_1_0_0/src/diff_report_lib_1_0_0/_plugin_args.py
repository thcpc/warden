class _PluginArgs:
    def __init__(self, args: dict):
        self.args = args.get("DiffReportPlugin")

    @property
    def task_id(self): return self.args.get("task_id")

    @property
    def left(self): return self.args.get("left")

    @property
    def right(self): return self.args.get("right")

    @property
    def compare_data(self): return self.args.get("compare_data")

    @property
    def title(self): return self.args.get("title")
