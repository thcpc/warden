import multiprocessing

from plugincore.database.config.database_info import DataBaseInfo
from plugincore.database.config.db_driver import DBDriver
from plugincore.database.support.database_api.db_thread import DBThread


class DBProcess:
    MAX_PARALLEL_WORKERS = 4

    def __init__(self, driver_info: dict):
        self.driver_info = driver_info

    def fetchmany_worker(self, driver_info, sqls):
        thread_db = DBThread(DBDriver(DataBaseInfo(driver_info)))
        return thread_db.fetchmany(sqls)

    def workers(self, sql_statements: list[str]):
        return [sql_statements[i:i + DBThread.MAX_CONCURRENT_THREAD] for i in
                range(0, len(sql_statements), DBThread.MAX_CONCURRENT_THREAD)]

    def fetchmany(self, sql_statements: list[str]):
        pool = multiprocessing.Pool(processes=DBProcess.MAX_PARALLEL_WORKERS)
        results = []
        apply_results = []
        for work in self.workers(sql_statements):
            result = pool.apply_async(self.fetchmany_worker, args=(self.driver_info,
                                                                   work))
            apply_results.append(result)
        pool.close()
        pool.join()
        for apply in apply_results:
            results.extend(apply.get())
        return results
