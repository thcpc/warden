import time

from plugincore.database.support.database_api.db_process import DBProcess
from plugincore.unit_tests.plugin_database.test_select_data import select_sqls, database_info_dict


def db_process_select():
    start = time.perf_counter()
    dg = DBProcess(database_info_dict)
    for r in dg.fetchmany(select_sqls):
        print(r)

    print(time.perf_counter() - start)


if __name__ == '__main__':
    db_process_select()
