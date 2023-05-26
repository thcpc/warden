from plugincore.plugin_run_record import PluginRunRecord


class PluginRunAudit:
    def __init__(self):
        self.plugin_records: list[PluginRunRecord] = []

    def add(self, record: PluginRunRecord):
        self.plugin_records.append(record)

    @property
    def ok(self):
        return len(list(filter(lambda record: not record.ok, self.plugin_records))) == 0

    @property
    def err_log(self):
        return list(filter(lambda record: not record.ok, self.plugin_records))

    def append(self, plugin_run_audit):
        for record in plugin_run_audit.plugin_records:
            self.plugin_records.append(record)

    def __str__(self):
        return "\n".join([str(record) for record in self.plugin_records])
