import multiprocessing

from plugincore.database.config.database_info import DataBaseInfo
from plugincore.database.config.db_driver import DBDriver


class DBProcess:
    MAX_PARALLEL_WORKERS = 2

    def __init__(self, drivers_info: list[dict]):
        self.drivers_info = drivers_info

    def fetchmany_worker(self, driver_info, sqls):
        thread_db = DBProcess(driver_info)
        return thread_db.fetchmany(sqls)

    def fetchmany(self, sql_statements: list[str]):
        pool = multiprocessing.Pool(processes=DBProcess.MAX_PARALLEL_WORKERS)
        results = []
        apply_results = []
        for driver in self.drivers_info:
            result = pool.apply_async(self.fetchmany_worker, args=(driver, sql_statements))
            apply_results.append(result)
        pool.close()
        pool.join()
        for apply in apply_results:
            results.extend(apply.get())
        return results