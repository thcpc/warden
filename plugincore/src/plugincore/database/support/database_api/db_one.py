from mysql.connector import OperationalError

from plugincore.database.config.db_driver import DBDriver
from plugincore.exceptions.plugin_fail_err import PluginFailErr


class DBOne:
    def __init__(self, db_driver: DBDriver):
        self.db_driver = db_driver

    def close(self):
        self.db_driver.close()

    def fetchmany(self, sql_statement):
        cursor = None
        connection = None
        try:
            connection = self.db_driver.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql_statement)

            values = cursor.fetchall()
            cols = [col[0] for col in cursor.description]
            data = [dict(zip(cols, ele)) for ele in values]
            return data
        except Exception as e:
            raise PluginFailErr(e)
        finally:
            self.final(cursor, connection)

    def final(self, cursor, connection):
        if cursor: cursor.close()
        if connection:
            try:
                connection.close()
            except OperationalError as e:
                pass

    def commit_blob(self, sql_statement_blob: str, spliter: str = ";\n"):
        sql_statements = sql_statement_blob.split(spliter)
        self.commit(sql_statements)

    def commit(self, sql_statements: list[str]):
        cursor = None
        connection = None
        try:
            connection = self.db_driver.get_connection()
            cursor = connection.cursor()

            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
            for sql in sql_statements:
                if sql.strip(): cursor.execute(sql.strip())
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise PluginFailErr(e)
        finally:
            self.final(cursor, connection)

    def procedure(self, sql_statement):
        cursor = None
        connection = None
        try:
            connection = self.db_driver.get_connection()
            cursor = connection.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            cursor.execute(sql_statement)
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise PluginFailErr(e)
        finally:
            self.final(cursor, connection)
