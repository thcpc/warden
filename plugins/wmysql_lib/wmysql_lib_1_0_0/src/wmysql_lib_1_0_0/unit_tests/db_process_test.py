import time

from wmysql_lib_1_0_0.support.db_process import DBProcess

from wmysql_lib_1_0_0.unit_tests.test_select_data import database_info_dict, select_sqls


def db_process_select():
    start = time.perf_counter()
    dg = DBProcess(database_info_dict)
    for r in dg.fetchmany(select_sqls):
        print(r)

    print(time.perf_counter() - start)


if __name__ == '__main__':
    db_process_select()
