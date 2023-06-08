import time

from wmysql_lib_1_0_0.config.db_driver import DBDriver
from wmysql_lib_1_0_0.support.db_thread import DBThread
from wmysql_lib_1_0_0.unit_tests.test_commit_data import commit_sqls
from wmysql_lib_1_0_0.unit_tests.test_select_data import database_info_dict, select_sqls
from wmysql_lib_1_0_0.wmysql_lib_plugin_form import DataBaseInfo


def db_thread_select():
    start = time.perf_counter()
    tdb = DBThread(db_driver=DBDriver(DataBaseInfo(database_info_dict)))
    for r in tdb.fetchmany(sql_statements=select_sqls):
        print(r)
    print(time.perf_counter() - start)

def db_thread_commit():
    start = time.perf_counter()
    tdb = DBThread(db_driver=DBDriver(DataBaseInfo(database_info_dict)))
    tdb.commit(commit_sqls)
    print(time.perf_counter() - start)


if __name__ == '__main__':
    db_thread_select()
    # db_thread_commit()
