import pkg_resources
from db_compare_1_0_0 import DbComparePlugin


def test_ref_plugin():
    p = DbComparePlugin()
    print(p.home)


def test_plugin_run():
    p = DbComparePlugin()
    p.run(databases=[
        {"operate": "DumpIn", "database_info": {
            "host": "dev-03-instance-1.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn",
            "user": "root",
            "pwd": "8YTJWOuA7XRK17wRQnw4",
            "port": 3306,
            "database": "eclinical_edc_dev_863"}, "sql_file": p.prepare_procedure},
        {"operate": "DumpIn", "database_info": {
            "host": "dev-03-instance-1.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn",
            "user": "root",
            "port": 3306,
            "pwd": "8YTJWOuA7XRK17wRQnw4",
            "database": "eclinical_edc_dev_864"}, "sql_file": p.prepare_procedure
         }])
    print(p.plugin_run_result)
