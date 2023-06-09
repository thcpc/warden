from wmysql_lib_1_0_0.config.db_driver import DBDriver
from wmysql_lib_1_0_0.support.database_api.db_one import DBOne
from wmysql_lib_1_0_0.support.database_api.db_process import DBProcess
from wmysql_lib_1_0_0.support.database_api.db_thread import DBThread


def factory(slq_count: int, db_driver: DBDriver):
    return clz(sql_count=slq_count)(db_driver)


def clz(sql_count: int):
    if sql_count < 10:
        return DBOne
    elif sql_count < 60:
        return DBThread
    else:
        return DBProcess
