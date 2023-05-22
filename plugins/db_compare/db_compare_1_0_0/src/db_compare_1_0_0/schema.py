import hashlib
import os

import cjen
from cjen import BigTangerine, DatabasePool
from cjen.bigtangerine import ContextArgs
from cjen.nene.helper import FileHelper

from db_compare_1_0_0.entities.ddl import DDL
from db_compare_1_0_0.entities.table import Table


class Schema(BigTangerine):
    def __init__(self, schema_info: dict):
        super().__init__()
        self.context["cursor"] = DatabasePool.cursor(host=schema_info.get("host"),
                                                     port=schema_info.get("port"),
                                                     user=schema_info.get("user"),
                                                     pwd=schema_info.get("pwd"),
                                                     database=schema_info.get("database"))
        self.context["table_dds"] = dict()

    @cjen.operate.mysql.factory(clazz=Table, size=-1, sql="SELECT DISTINCT TABLE_NAME as name FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME NOT LIKE 'vw%';")
    def load(self, tables: list[Table] = None, **kwargs):
        for table in tables:
            self.context["table_name"] = table.name()
            self.get_ddls()

    @cjen.operate.mysql.factory(clazz=DDL, sql=FileHelper.cur_read(cur=__file__, file=os.path.join("resources/get_ddl.sql")), params=ContextArgs(table_name="table_name"), track=True)
    def get_ddls(self, ddl: DDL = None, **kwargs):
        if ddl.Table():
            self.context["table_dds"][ddl.Table()] = {"ddl": ddl.meta_data.get("Create Table"),
                                                      "sha1": hashlib.sha1(ddl.meta_data.get("Create Table").encode("utf-8")).hexdigest()}
        elif ddl.View():
            self.context["table_dds"][ddl.View()] = {"ddl": ddl.meta_data.get("Create View"),
                                                     "sha1": hashlib.sha1(ddl.meta_data.get("Create View").encode("utf-8")).hexdigest()}
        else:
            pass

    def length(self):
        return len(self.context["table_dds"])

    def tables(self) -> list[str]:
        return list(self.context["table_dds"].keys())

    def get_table_by_index(self, index):
        return self.tables()[index]

    def ddl_of(self, table_name) -> str:
        return self.context["table_dds"].get(table_name).get("ddl")

    def sha1_of(self, table_name):
        return self.context["table_dds"].get(table_name).get("sha1")

    # def compare_with(self, database):
    #     from helper.sql_testing.tasks.compare_task import CompareTask
    #     self.load()
    #     database.load()
    #     ct = CompareTask(self, database)
    #     ct.run()
    #     return ct.result