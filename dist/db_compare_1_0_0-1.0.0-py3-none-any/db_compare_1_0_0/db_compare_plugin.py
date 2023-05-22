import os.path
from os import path

from jinja2 import FileSystemLoader, Environment
from plugincore import Plugin
from db_compare_1_0_0.compare.compare_task import CompareTask
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

    def task(self, *args, **kwargs):
        left = Schema(kwargs.get("databases")[0].get("database_info"))
        left.load()
        right = Schema(kwargs.get("databases")[1].get("database_info"))
        right.load()
        compare_task = CompareTask(left=left, right=right)
        compare_task.run()
        print(compare_task.result)


