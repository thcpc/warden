import cjen
from cjen import MetaMysql


class Table(MetaMysql):
    @cjen.operate.common.value
    def name(self): ...
