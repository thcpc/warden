import os.path
from os import path

from jinja2 import FileSystemLoader, Environment
from plugincore import Plugin

from db_compare_1_0_0.compare.compare_task import CompareTask
from db_compare_1_0_0.db_compare_plugin_form import DbComparePluginForm
from db_compare_1_0_0.schema import Schema


class DbComparePlugin(Plugin):

    def __init__(self):
        super().__init__(abs_path=path.dirname(__file__))

    @property
    def home(self):
        loader = FileSystemLoader(searchpath=os.path.join(path.dirname(__file__), "resources"))
        env = Environment(loader=loader)
        template = env.get_template("home.jinjia.html")

        return template.render()

    @property
    def prepare_procedure(self):
        return os.path.join(path.dirname(__file__), "resources", "get_ddl_procedure.sql")

    def task(self, form_data: dict):
        plugin_form = DbComparePluginForm(self, form_data)
        compare_task = CompareTask([Schema(database).load() for database in plugin_form.databases])
        compare_task.run()
        form_data["diff_report_lib"]["compare_data"] = compare_task.result
        self.audit(dict(status=200, msg=f"{self.id} {compare_task.msg()} finish"))

    def estimate(self, form_data) -> int:
        return super().estimate(form_data) + 1
