
from os import path


from plugincore import Plugin
from plugincore import PluginRunLog
from wmysql_1_0_0.operate.dump_in import DumpIn
from wmysql_1_0_0.operate.dump_out import DumpOut


class WMysqlPlugin(Plugin):

    def __init__(self):
        super().__init__(abs_path=path.dirname(__file__))

    """
    参数
    **kwargs: databases: list[dict]
    database: 
        operate: DumpIn 执行， DumpOut 导出
        database_info: dict , 数据库信息
            user: 用户名
            host: 数据库服务器
            pwd: 密码
            database: 数据库名
        sql_file: 执行的数据库文件
    """
    def task(self, *args, **kwargs):

        for arg in kwargs.get("databases"):
            dump = {"DumpIn": DumpIn, "DumpOut": DumpOut}.get(arg.get("operate"))
            res = dump(self.mysql_exe(arg.get("operate")), arg.get("database_info")).exec(arg.get("sql_file"))
            self.add_log(res)

    def add_log(self, res):
        log = PluginRunLog() << res << {"plugin.id": self.id, "plugin.version": self.version}
        self.plugin_run_result.add(log)

    def mysql_exe(self, operate: str):
        exec_name = {"DumpIn": "mysql", "DumpOut": "mysql_dump"}.get(operate)
        env = self.config.get("env")
        return self.config.get(env).get(exec_name)


