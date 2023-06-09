

import pkg_resources

from wmysql_lib_1_0_0.wmysql_lib_plugin import WMysqlLibPlugin


def create_plugin() -> WMysqlLibPlugin:
    for entry_point in pkg_resources.iter_entry_points('wmysql_lib_1_0_0.plugin'):
        return entry_point.load()()


def test_ref_plugin():
    w = create_plugin()
    r = w.run(form_data=dict(wmysql_lib=dict(database_ops=[dict(operate="DumpIn",
               database_info={
                   "host": "dev-03-instance-1.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn",
                   "user": "root",
                   "pwd": "8YTJWOuA7XRK17wRQnw4",
                   "database": "eclinical_edc_dev_860"

               }, sql_file="D:\\github\\warden\\plugins\\wmysql_lib\\wmysql_lib_1_0_0\\integration_tests\\get_ddl_produre.sql")])))
    print(r)
