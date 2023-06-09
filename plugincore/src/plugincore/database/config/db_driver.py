# import pymysql
# from dbutils.pooled_db import PooledDB
import mysql.connector


from plugincore.exceptions.plugin_fail_err import PluginFailErr


class DBDriver:
    def __init__(self, database_info, pool_size=1):
        try:
            self.cnx_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool",
                                                                        pool_size=pool_size,
                                                                        **database_info)
        except mysql.connector.Error as err:
            raise PluginFailErr(err)

    def get_connection(self):
        return self.cnx_pool.get_connection()

    def close(self): ...
