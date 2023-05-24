import sys

import pkg_resources
from cjen.nene.helper import FileHelper
from wmysql_1_0_0 import WMysqlPlugin

print("----------",sys.path)

def create_plugin() -> WMysqlPlugin:
    for entry_point in pkg_resources.iter_entry_points('wmysql_1_0_0.plugin'):
        return entry_point.load()()

def test_ref_plugin():
   w = create_plugin()
   print(w.id)

   # r= w.task(operate="DumpIn", database_info={
   #     "host":"dev-03-instance-1.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn",
   #     "user":"root",
   #     "pwd":"8YTJWOuA7XRK17wRQnw4",
   #     "database": "eclinical_edc_dev_860"
   #
   # }, sql_file="D:\\github\\warden\\plugins\\wmysql\\wmysql_1_0_0\\tests\\get_ddl_produre.sql")
   # print(r)
