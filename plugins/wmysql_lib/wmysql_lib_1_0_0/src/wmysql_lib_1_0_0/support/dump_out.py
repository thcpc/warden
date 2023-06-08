import os
import subprocess


class DumpOut:
    def __init__(self, mysql_exe, database_info):
        self.database_info = database_info
        self.mysql_exe = mysql_exe
        self.cmd_template = "\"{mysqldump_exe}\" -u{u} -p{p} --host={h} --protocol=tcp --column-statistics=FALSE --port=3306 --default-character-set=utf8 --routines --skip-triggers \"{dbname}\"> {sql_path}"

    def command(self, sql_file):
        return self.cmd_template.format(mysqldump_exe=self.mysql_exe,
                                        u=self.database_info.user,
                                        p=self.database_info.pwd,
                                        h=self.database_info.host,
                                        sql_path=sql_file,
                                        dbname=self.database_info.database)

    def exec(self, sql_file):
        if not os.path.exists(sql_file): raise {"status": -100, "err": f"no {sql_file}"}
        ret = subprocess.getstatusoutput(self.command(sql_file))
        if ret[0] != 0:
            return {"status": -100, "err": ret[1]}
        return {"status": 200}