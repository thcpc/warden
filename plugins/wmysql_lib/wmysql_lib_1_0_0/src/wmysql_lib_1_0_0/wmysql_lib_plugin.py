
from os import path


from plugincore import Plugin
from plugincore.database.support.mysql_dump.dump_in import DumpIn
from plugincore.database.support.mysql_dump.dump_out import DumpOut

from wmysql_lib_1_0_0.properties.form.wmysql_lib_plugin_form import WmysqlLibPluginForm


class WMysqlLibPlugin(Plugin):

    def __init__(self):
        super().__init__(abs_path=path.dirname(__file__))

    def processor(self, form_data: dict):
        plugin_form = WmysqlLibPluginForm(self, form_data)
        for op in plugin_form.database_ops:
            dump = {"DumpIn": DumpIn, "DumpOut": DumpOut}.get(op.operate)
            dump(mysql_exe=self.mysql_exe(op.operate), database_info=op.database_info).exec(op.sql_file)
            self.audit(dict(status=200, msg=f'{self.id} {op.operate} {op.database_info} finish'))

    def mysql_exe(self, operate: str):
        exec_name = {"DumpIn": "mysql", "DumpOut": "mysql_dump"}.get(operate)
        env = self.config.get("env")
        return self.config.get(env).get(exec_name)

    def estimate(self, form_data) -> int:
        plugin_form = WmysqlLibPluginForm(self, form_data)
        return len(plugin_form.database_ops) + super().estimate(form_data)


