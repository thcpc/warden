import cjen
from cjen import MetaMysql


class DDL(MetaMysql):
    @cjen.operate.common.value
    def Table(self): ...

    @cjen.operate.common.value
    def View(self): ...