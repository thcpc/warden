import os
import subprocess


class DumpIn:
    def __init__(self, mysql_exe, database_info: dict):
        self.database_info = database_info
        self.mysql_exe = mysql_exe
        self.cmd_template = "\"{mysql_exe}\" -u{u} -p{p} {dbname} -h{h} < {sql_path}"

    def command(self, sql_file):
        return self.cmd_template.format(mysql_exe=self.mysql_exe,
                                        u=self.database_info.get("user"),
                                        p=self.database_info.get("pwd"),
                                        h=self.database_info.get("host"),
                                        sql_path=sql_file,
                                        dbname=self.database_info.get("database"))

    def exec(self, sql_file):
        if not os.path.exists(sql_file): return {"status": -100, "err": f"no {sql_file}"}
        ret = subprocess.getstatusoutput(self.command(sql_file))
        if ret[0] != 0:
            return {"status": -100, "err": ret[1]}
        return {"status": 200}
