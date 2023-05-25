from os import path

from plugincore import Plugin

from diff_report_lib_1_0_0._plugin_args import _PluginArgs
from diff_report_lib_1_0_0.html.html_factory import HtmlFactory


class DiffReportLibPlugin(Plugin):

    def __init__(self):
        super().__init__(abs_path=path.dirname(__file__))

    @property
    def env(self): return self.config.get("env", 'prod')

    def task(self, *args, **kwargs):
        HtmlFactory(_PluginArgs(kwargs)).gen(self.env)
