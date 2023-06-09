from cjen.nene.properties import required
from plugincore.exceptions.plugin_running_args_err import PluginRunningArgsErr


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

    @property
    @required(exception_class=PluginRunningArgsErr, err_msg='DataBaseInfo\'s port Required')
    def port(self): return self.info.get("port")

    def __str__(self): return str(self.info)