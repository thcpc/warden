from cjen.nene.properties import required
from plugincore.exceptions.plugin_running_args_err import PluginRunningArgsErr

from wmysql_lib_1_0_0.config.database_info import DataBaseInfo


class DataBaseOp:
    def __init__(self, op: dict):
        self.op = op

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DataBaseOp\'s operate Required')
    def operate(self):
        return self.op.get("operate")

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DataBaseOp\'s database_info Required')
    def database_info(self):
        return DataBaseInfo(self.op.get("database_info"))

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DataBaseOp\'s sql_file Required')
    def sql_file(self):
        return self.op.get("sql_file")