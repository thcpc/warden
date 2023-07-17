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
            diff_form = DiffReportLibPluginForm(self, form_data)
            HtmlFactory(diff_form).gen(self.env)
            self.audit(dict(status=200, msg=f'{self.id} create report {diff_form.title} finish'))
        except Exception as e:
            raise PluginFailErr(e)

    """
    如果在task 添加了 audit, 则在计算步骤的时候，需增加一个父类的estimate
    """
    def estimate(self, form_data) -> int:
        return super().estimate(form_data) + 1

