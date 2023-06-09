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
    def pwd(self):
        return self.info.get("pwd")

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DataBaseInfo\'s port Required')
    def port(self): return self.info.get("port")

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DataBaseInfo\'s database Required')
    def database(self): return self.info.get("database")

    def __str__(self): return str(self.info)


class DbComparePluginForm(PluginForm):

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DbComparePluginForm\'s database_ops Required')
    def databases(self):
        if self.form_data.get("databases") is None: return None
        return [DataBaseInfo(data) for data in self.form_data.get("databases")]
