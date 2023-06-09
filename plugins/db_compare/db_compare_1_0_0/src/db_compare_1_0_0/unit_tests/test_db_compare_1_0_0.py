import pkg_resources
from db_compare_1_0_0 import DbComparePlugin


def test_ref_plugin():
    p = DbComparePlugin()
    print(p.home)


def test_plugin_run():
    p = DbComparePlugin()
    form_data = {p.id: dict(databases=[{"host": "dev-03-instance-1.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn",
                                        "user": "root",
                                        "pwd": "8YTJWOuA7XRK17wRQnw4",
                                        "port": 3306,
                                        "database": "eclinical_edc_dev_860"},
                                       {"host": "dev-03-instance-1.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn",
                                        "user": "root",
                                        "port": 3306,
                                        "pwd": "8YTJWOuA7XRK17wRQnw4",
                                        "database": "eclinical_edc_dev_863"}]),
                 "wmysql_lib": dict(database_ops=[dict(operate="DumpIn",
                                                       database_info={
                                                           "host": "dev-03-instance-1.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn",
                                                           "user": "root",
                                                           "port": 3306,
                                                           "pwd": "8YTJWOuA7XRK17wRQnw4",
                                                           "database": "eclinical_edc_dev_860"

                                                       }, sql_file=p.prepare_procedure),
                                                  dict(operate="DumpIn",
                                                       database_info={
                                                           "host": "dev-03-instance-1.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn",
                                                           "user": "root",
                                                           "port": 3306,
                                                           "pwd": "8YTJWOuA7XRK17wRQnw4",
                                                           "database": "eclinical_edc_dev_863"

                                                       }, sql_file=p.prepare_procedure)
                                                  ]),
                 "diff_report_lib": dict(task_id=11111, title="测试", left="xxxxxx", right="ddddddd")}
    p.run(form_data=form_data, need_estimate=True)
    # p.run(form_data=dict(databases=[{},{}
    #
    #     {"operate": "DumpIn", "database_info": {
    #         "host": "dev-03-instance-1.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn",
    #         "user": "root",
    #         "pwd": "8YTJWOuA7XRK17wRQnw4",
    #         "port": 3306,
    #         "database": "eclinical_edc_dev_863"}, "sql_file": p.prepare_procedure},
    #     {"operate": "DumpIn", "database_info": {
    #         "host": "dev-03-instance-1.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn",
    #         "user": "root",
    #         "port": 3306,
    #         "pwd": "8YTJWOuA7XRK17wRQnw4",
    #         "database": "eclinical_edc_dev_864"}, "sql_file": p.prepare_procedure
    #      }]))
    print(p.plugin_run_audit)
    print(p.step_count)
