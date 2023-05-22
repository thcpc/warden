class PluginRunLog:
    def __init__(self):
        self.record = {}

    def __lshift__(self, other):
        self.record.update(other)
        return self

    @property
    def ok(self): return self.record.get("status") == 200

    @property
    def plugin_id(self): return self.record.get("plugin.id")

    @property
    def plugin_version(self): return self.record.get("plugin.version")

    @property
    def err(self): return self.record.get("err")

    @property
    def all(self): return self.record

    def __str__(self):
        return str(self.record)
