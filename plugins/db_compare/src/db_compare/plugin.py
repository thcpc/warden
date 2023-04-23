import os.path
from os import path

from pkg_resources import resource_filename


class Plugin:
    @property
    def name(self): return "表结构比对"

    @property
    def home(self):
        with open(os.path.join(path.dirname(__file__),"resources", "home.jinjia.html"), mode='r', encoding='utf-8') as f:
        # with open(resource_filename("db_compare", os.path.join("resources", "home.jinjia.html")), mode='r',
        #           encoding='utf-8') as f:
            return f.read()

if __name__ == '__main__':
    print(Plugin().home)