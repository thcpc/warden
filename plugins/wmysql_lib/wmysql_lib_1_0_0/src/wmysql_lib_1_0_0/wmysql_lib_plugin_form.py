from cjen.nene.properties import required
from plugincore.exceptions.plugin_running_args_err import PluginRunningArgsErr
from plugincore.plugin_form import PluginForm

from wmysql_lib_1_0_0.config.database_op import DataBaseOp


class WmysqlLibPluginForm(PluginForm):
    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='WmysqlLibPluginForm\'s database_ops Required')
    def database_ops(self):
        if self.form_data.get("database_ops") is None: return None
        return [DataBaseOp(data) for data in self.form_data.get("database_ops")]
