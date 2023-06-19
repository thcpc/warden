import time

from plugincore.database.config.database_info import DataBaseInfo
from plugincore.database.config.db_driver import DBDriver
from plugincore.database.support.database_api.db_thread import DBThread
from plugincore.unit_tests.plugin_database.test_commit_data import commit_sqls
from plugincore.unit_tests.plugin_database.test_select_data import database_info_dict, select_sqls


def db_thread_select():
    start = time.perf_counter()
    tdb = DBThread(db_driver=DBDriver(database_info_dict))
    print(time.perf_counter() - start)
    start = time.perf_counter()
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
