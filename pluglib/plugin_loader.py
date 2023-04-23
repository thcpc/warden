import importlib
from requests import get

class PlugInLoader:
    def __init__(self, pkgs: list):
       self.requests = importlib.import_module('get')

    def run(self):
        r = self.requests("http://dev-01-app-01.chengdudev.edetekapps.cn/html/admin/assets/i18n/en_US/translations.json?_v=1682218604521")
        # r = self.requests.get("http://dev-01-app-01.chengdudev.edetekapps.cn/html/admin/assets/i18n/en_US/translations.json?_v=1682218604521")
        print(r.content)

if __name__ == '__main__':
    pl = PlugInLoader([])
    pl.run()