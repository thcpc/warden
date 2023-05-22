from plugincore.plugin_run_log import PluginRunLog


class PluginRunResult:
    def __init__(self):
        self.plugin_logs: list[PluginRunLog] = []

    def add(self, plugin_log: PluginRunLog):
        self.plugin_logs.append(plugin_log)


    @property
    def ok(self):
        return len(list(filter(lambda log: not log.ok, self.plugin_logs))) == 0

    @property
    def err_log(self):
        return list(filter(lambda log: not log.ok, self.plugin_logs))

    def append(self, plugin_run_result):
        for log in plugin_run_result.plugin_logs:
            self.plugin_logs.append(log)

    def __str__(self):
        return "\n".join([str(log) for log in self.plugin_logs])
