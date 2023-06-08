import pymysql
from dbutils.pooled_db import PooledDB


class DBDriver:
    def __init__(self, database_info):
        self.database_info = database_info
        self.pool_db = PooledDB(
            creator=pymysql,
            maxconnections=20,
            mincached=10,
            maxcached=10,
            blocking=True,
            host=database_info.host,
            port=database_info.port,
            user=database_info.user,
            password=database_info.pwd,
            database=database_info.database,
            charset='utf8mb4',
        )
        self.connection = None

    def get_connection(self): return self.pool_db.connection()

    def close(self): self.pool_db.close()
