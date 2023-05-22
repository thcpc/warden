import os.path
from os import path

from jinja2 import FileSystemLoader, Environment
from plugincore import Plugin


class DiffReportPlugin(Plugin):

    def __init__(self):
        super().__init__(abs_path=path.dirname(__file__))

    @property
    def home(self): ...



    def task(self, *args, **kwargs):
        loader = FileSystemLoader(searchpath=os.path.join(path.dirname(__file__), "resources"))
        env = Environment(loader=loader)
        template = env.get_template("home.jinjia.html")

        return template.render()
