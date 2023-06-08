
from concurrent.futures import ThreadPoolExecutor, as_completed
from wmysql_lib_1_0_0.config.db_driver import DBDriver
from wmysql_lib_1_0_0.support.db_one import DBOne


class DBThread:
    MAX_CONCURRENT_THREAD = 20
    MAX_PARALLEL_THREAD = 5

    def __init__(self, db_driver: DBDriver):
        self.db_driver = db_driver
        self.executor = ThreadPoolExecutor(max_workers=DBThread.MAX_PARALLEL_THREAD)
        self.queries = []

    def fetchmany(self, sql_statements: list[str]):
        db_one = DBOne(self.db_driver)
        thread_list = []
        while sql_statements:
            thread = self.executor.submit(db_one.fetchmany, sql_statements.pop())
            thread_list.append(thread)
        for task in as_completed(thread_list):
            self.queries.append(task.result()[0])
        return self.queries

    def commit(self, sql_statements: list[str]):
        db_one = DBOne(self.db_driver)
        thread_list = []
        while sql_statements:
            thread = self.executor.submit(db_one.commit, sql_statements.pop())
            thread_list.append(thread)
        for task in as_completed(thread_list):
            self.queries.append(task.result()[0])
