
from concurrent.futures import ThreadPoolExecutor, as_completed

from plugincore.database.config.db_driver import DBDriver
from plugincore.database.support.database_api.db_one import DBOne


class DBThread:
    MAX_CONCURRENT_THREAD = 20
    MAX_PARALLEL_THREAD = 5

    def __init__(self, db_driver: DBDriver):
        self.db_driver = db_driver
        self.queries = []

    def fetchmany(self, sql_statements: list[str]):
        db_one = DBOne(self.db_driver)
        executor = ThreadPoolExecutor(max_workers=DBThread.MAX_PARALLEL_THREAD)
        thread_list = []
        while sql_statements:
            thread = executor.submit(db_one.fetchmany, sql_statements.pop())
            thread_list.append(thread)
        for task in as_completed(thread_list):
            self.queries.append(task.result()[0])
        executor.shutdown(wait=True)
        # db_one.close()
        return self.queries

    # 只是为了保证接口统一并不处理
    def close(self): ...

    def commit(self, sql_statements: list[str]):
        db_one = DBOne(self.db_driver)
        executor = ThreadPoolExecutor(max_workers=DBThread.MAX_PARALLEL_THREAD)
        thread_list = []
        while sql_statements:
            thread = executor.submit(db_one.commit, sql_statements.pop())
            thread_list.append(thread)
        for task in as_completed(thread_list):
            self.queries.append(task.result()[0])
        db_one.close()
