import time

from plugincore.database.config.database_info import DataBaseInfo
from plugincore.database.support.database_api.db_one import DBOne
from plugincore.database.config.db_driver import DBDriver
from plugincore.unit_tests.plugin_database.test_commit_data import commit_sqls, procedure_sql
from plugincore.unit_tests.plugin_database.test_select_data import database_info_dict


def db_one_select():
    start = time.perf_counter()
    tdb = DBOne(db_driver=DBDriver(DataBaseInfo(database_info_dict)))
    print(tdb.fetchmany(sql_statement="call GET_DDL('eclinical_study');"))
    # for sql in select_sqls:
    #     print(tdb.fetchmany(sql_statement=sql, where=None))
    print(time.perf_counter() - start)


def db_one_commit():
    start = time.perf_counter()
    tdb = DBOne(db_driver=DBDriver(DataBaseInfo(database_info_dict)))
    for sql in commit_sqls:
        tdb.commit(sql)
    print(time.perf_counter() - start)


def db_one_procedure():
    start = time.perf_counter()
    tdb = DBOne(db_driver=DBDriver(DataBaseInfo(database_info_dict)))
    tdb.procedure(procedure_sql)
    print(time.perf_counter() - start)


if __name__ == '__main__':
    # db_one_commit()
    db_one_select()
    # db_one_procedure()
