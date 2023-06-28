import os
import subprocess

from plugincore.exceptions.plugin_fail_err import PluginFailErr


class DumpIn:
    def __init__(self, *, mysql_exe, database_info):
        self.database_info = database_info
        self.mysql_exe = mysql_exe
        self.cmd_template = "\"{mysql_exe}\" -u{u} -p{p} {dbname} -h{h} -P {P}< {sql_path}"

    def command(self, sql_file):
        return self.cmd_template.format(mysql_exe=self.mysql_exe,
                                        u=self.database_info.user,
                                        p=self.database_info.pwd,
                                        h=self.database_info.host,
                                        P=self.database_info.port,
                                        sql_path=sql_file,
                                        dbname=self.database_info.database)

    def exec(self, sql_file):
        if not os.path.exists(sql_file): raise PluginFailErr(f"can not find {sql_file}")
        ret = subprocess.getstatusoutput(self.command(sql_file))
        if ret[0] != 0: raise PluginFailErr(ret[1])
        return {"status": 200}
