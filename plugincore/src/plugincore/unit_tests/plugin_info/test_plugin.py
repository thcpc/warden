import os

from plugincore.plugin import Plugin
from plugincore.plugin_run_log import PluginRunLog


class CustomPlugin(Plugin):
    def __init__(self):
        super().__init__(os.path.dirname(__file__))

    def task(self, *args, **kwargs):
        log = PluginRunLog() << {"status": 200 } << {"plugin.id": self.id, "plugin.version": self.version}
        self.plugin_run_result.add(log)


def test_plugin_info():
    p = CustomPlugin()
    assert p.id, "tsc"
    assert p.name, "表结构对比"
    assert p.description, "数据库结构比对工具，主要用来比对指定的两个 schema 的结构是否一致"
    assert p.version, "1_0_0"
    assert p.before_plugins[0].get("plugin_id"), 'btest1'
    assert p.before_plugins[0].get("version"), 100
    assert p.before_plugins[1].get("plugin_id"), 'btest2'
    assert p.before_plugins[1].get("version"), 101
    assert p.after_plugins[0].get("plugin_id"), 'atest1'
    assert p.after_plugins[0].get("version"), '1_0_0'
    assert p.after_plugins[1].get("plugin_id"), 'atest2'
    assert p.after_plugins[1].get("version"), '1_0_1'

