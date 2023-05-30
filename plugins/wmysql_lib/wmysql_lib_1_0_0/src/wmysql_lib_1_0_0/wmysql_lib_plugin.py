
from os import path


from plugincore import Plugin

from wmysql_lib_1_0_0.operate.dump_in import DumpIn
from wmysql_lib_1_0_0.operate.dump_out import DumpOut
from wmysql_lib_1_0_0.wmysql_lib_plugin_form import WmysqlLibPluginForm


class WMysqlLibPlugin(Plugin):

    def __init__(self):
        super().__init__(abs_path=path.dirname(__file__))

    def task(self, form_data: dict):
        plugin_form = WmysqlLibPluginForm(self, form_data)
        for op in plugin_form.database_ops:
            dump = {"DumpIn": DumpIn, "DumpOut": DumpOut}.get(op.operate)
            dump(mysql_exe=self.mysql_exe(op.operate), database_info=op.database_info).exec(op.sql_file)

    def mysql_exe(self, operate: str):
        exec_name = {"DumpIn": "mysql", "DumpOut": "mysql_dump"}.get(operate)
        env = self.config.get("env")
        return self.config.get(env).get(exec_name)


