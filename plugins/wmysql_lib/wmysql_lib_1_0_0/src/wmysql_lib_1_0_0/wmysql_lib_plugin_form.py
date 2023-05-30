from cjen.nene.properties import required
from plugincore.exceptions.plugin_running_args_err import PluginRunningArgsErr
from plugincore.plugin_form import PluginForm


class DataBaseInfo:
    def __init__(self, info: dict):
        self.info = info

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DataBaseInfo\'s user Required')
    def user(self): return self.info.get("user")

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DataBaseInfo\'s host Required')
    def host(self): return self.info.get("host")

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DataBaseInfo\'s pwd Required')
    def pwd(self): return self.info.get("pwd")

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DataBaseInfo\'s database Required')
    def database(self): return self.info.get("database")


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


class WmysqlLibPluginForm(PluginForm):
    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='WmysqlLibPluginForm\'s database_ops Required')
    def database_ops(self):
        return [DataBaseOp(data) for data in self.form_data.get("database_ops")]
