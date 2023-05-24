import os.path
from os import path

from jinja2 import FileSystemLoader, Environment
from plugincore import Plugin

from diff_report_1_0_0._plugin_args import _PluginArgs
from diff_report_1_0_0.viwe_factory import ViewFactory


class DiffReportPlugin(Plugin):

    def __init__(self):
        super().__init__(abs_path=path.dirname(__file__))

    @property
    def home(self): ...

    def task(self, *args, **kwargs):
        ViewFactory(_PluginArgs(kwargs)).gen()

