from os import path

from plugincore import Plugin
from plugincore.exceptions.plugin_fail_err import PluginFailErr

from config_lib_1_0_0.diff_report_lib_plugin_form import DiffReportLibPluginForm


class ConfigLibPlugin(Plugin):

    def __init__(self):
        super().__init__(abs_path=path.dirname(__file__))

    @property
    def env(self): return self.config.get("env", 'prod')




    def estimate(self, form_data) -> int:
        return super().estimate(form_data) + 1

