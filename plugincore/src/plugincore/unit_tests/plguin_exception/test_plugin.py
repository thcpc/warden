import os

from plugincore.plugin import Plugin
from plugincore.plugin_run_record import PluginRunRecord


class CustomPlugin(Plugin):
    def __init__(self):
        super().__init__(os.path.dirname(__file__))

    def processor(self, form_data: dict):
        record = PluginRunRecord() << {"status": 200} << {"plugin.id": self.id, "plugin.version": self.version}
        self.plugin_run_audit.add(record)


class CustomPlugin1(Plugin):
    def __init__(self):
        super().__init__(os.path.dirname(__file__))

    def processor(self, form_data: dict):
        record = PluginRunRecord() << {"status": -100, "err": "Test Error "} << {"plugin.id": self.id,
                                                                        "plugin.version": self.version}
        self.plugin_run_audit.add(record)


def test_plugin_run():
    p = CustomPlugin()
    audit = p.run(dict())
    assert audit.ok==False
    print(audit)
    p = CustomPlugin1()
    audit = p.run(dict())
    assert audit.ok==False
    print(audit)