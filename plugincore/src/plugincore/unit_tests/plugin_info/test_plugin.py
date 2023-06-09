import os

from plugincore.plugin import Plugin


from plugincore.plugin_run_record import PluginRunRecord


class CustomPlugin(Plugin):
    def __init__(self):
        super().__init__(os.path.dirname(__file__))

    def processor(self, *args, **kwargs):
        log = PluginRunRecord() << {"status": 200 } << {"plugin.id": self.id, "plugin.version": self.version}
        self.plugin_run_audit.add(log)


def test_plugin_info():
    p = CustomPlugin()
    assert p.id, "tsc"
    assert p.name, "表结构对比"
    assert p.description, "数据库结构比对工具，主要用来比对指定的两个 schema 的结构是否一致"
    assert p.version, "1_0_0"
    assert p.dependence[0].processor, 'processor1'
    assert p.dependence[0].plugin_id, 'btest1'
    assert p.dependence[0].version, "1_0_0"
    assert p.dependence[1].processor, 'processor2'
    assert p.dependence[1].plugin_id, 'btest2'
    assert p.dependence[1].version, "1_0_1"

