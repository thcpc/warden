import os

from plugincore.plugin import Plugin
from plugincore.plugin_run_log import PluginRunLog


class CustomPlugin(Plugin):
    def __init__(self):
        super().__init__(os.path.dirname(__file__))

    def task(self, *args, **kwargs):
        log = PluginRunLog() << {"status": 200} << {"plugin.id": self.id, "plugin.version": self.version}
        self.plugin_run_result.add(log)


class CustomPlugin1(Plugin):
    def __init__(self):
        super().__init__(os.path.dirname(__file__))

    def task(self, *args, **kwargs):
        log = PluginRunLog() << {"status": -100, "err": "Test Error "} << {"plugin.id": self.id,
                                                                        "plugin.version": self.version}
        self.plugin_run_result.add(log)


def test_plugin_run():
    p = CustomPlugin()
    assert p.run().ok, True
    p = CustomPlugin1()
    assert p.run().ok == False