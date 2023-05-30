from os import path

from plugincore import Plugin
from plugincore.exceptions.plugin_fail_err import PluginFailErr

from diff_report_lib_1_0_0.diff_report_lib_plugin_form import DiffReportLibPluginForm
from diff_report_lib_1_0_0.html.html_factory import HtmlFactory


class DiffReportLibPlugin(Plugin):

    def __init__(self):
        super().__init__(abs_path=path.dirname(__file__))

    @property
    def env(self): return self.config.get("env", 'prod')

    def task(self, form_data: dict):
        try:
            HtmlFactory(DiffReportLibPluginForm(self, form_data)).gen(self.env)
        except Exception as e:
            raise PluginFailErr(e)
