import os

from plugin import Plugin


class CustomPlugin(Plugin):
    def __init__(self):
        super().__init__(os.path.dirname(__file__))


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
