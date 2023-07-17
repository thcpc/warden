import os

from tqdm import tqdm

from plugincore.database.config.database_info import DataBaseInfo
from plugincore.database.support.mysql_dump.dump_in import DumpIn

root = "C:\\Users\\PengchengChen\\Desktop\\audit"
# for fn in os.listdir(root):
#     print(f'create database {fn.replace(".sql", "")};')

database_info = DataBaseInfo(dict(
    host="automation-01.chengdudev.edetekapps.cn ", port=3307,
    user='root', pwd='123456', database='eclinical_edc_prod_1'
))


def exclude():
    # eclinical_edc_prod_11.sql
    # eclinical_edc_prod_21.sql
    # eclinical_edc_prod_28.sql
    # eclinical_edc_prod_6.sql
    return [
        'eclinical_edc_prod_11.sql',
        'eclinical_edc_prod_21.sql',
        'eclinical_edc_prod_28.sql',
        'eclinical_edc_prod_6.sql']
    # return ['eclinical_edc_prod_11.sql',
    #         'eclinical_edc_prod_1.sql',
    #         'eclinical_edc_prod_10.sql',
    #         'eclinical_edc_prod_100.sql',
    #         'eclinical_edc_prod_101.sql',
    #         'eclinical_edc_prod_102.sql',
    #         'eclinical_edc_prod_104.sql',
    #         'eclinical_edc_prod_105.sql',
    #         'eclinical_edc_prod_106.sql',
    #         'eclinical_edc_prod_107.sql',
    #         'eclinical_edc_prod_109.sql',
    #         'eclinical_edc_prod_110.sql',
    #         'eclinical_edc_prod_111.sql',
    #         'eclinical_edc_prod_113.sql',
    #         'eclinical_edc_prod_114.sql',
    #         'eclinical_edc_prod_115.sql',
    #         'eclinical_edc_prod_118.sql',
    #         'eclinical_edc_prod_119.sql',
    #         'eclinical_edc_prod_12.sql',
    #         'eclinical_edc_prod_120.sql',
    #         'eclinical_edc_prod_127.sql',
    #         'eclinical_edc_prod_128.sql',
    #         'eclinical_edc_prod_129.sql',
    #         'eclinical_edc_prod_13.sql',
    #         'eclinical_edc_prod_136.sql',
    #         'eclinical_edc_prod_14.sql',
    #         'eclinical_edc_prod_15.sql',
    #         'eclinical_edc_prod_16.sql',
    #         'eclinical_edc_prod_17.sql',
    #         'eclinical_edc_prod_18.sql',
    #         'eclinical_edc_prod_19.sql',
    #         'eclinical_edc_prod_2.sql',
    #         'eclinical_edc_prod_21.sql',
    #         'eclinical_edc_prod_28.sql',
    #         'eclinical_edc_prod_6.sql']


def sql_files():
    result = []
    for fn in os.listdir(root):
        if fn.endswith(".sql") and fn not in exclude():
            result.append(fn)
    return result


def dump(database_info, sql_file):
    with open("dump.log", "a") as f:
        f.write(f"{sql_file} BEGIN\n")
    di = DumpIn(mysql_exe="C:\\mysql-8.0.31-winx64\\bin\\mysql", database_info=database_info)
    di.exec(os.path.join(root, sql_file))
    with open("dump.log", "a") as f:
        f.write(f"{sql_file} END\n")


if __name__ == '__main__':
    common_database = dict(
        host="automation-01.chengdudev.edetekapps.cn ", port=3307,
        user='root', pwd='123456')

    pbar = tqdm(sql_files())
    for sql_file in pbar:
        common_database["database"] = sql_file.replace(".sql", "")
        dump(DataBaseInfo(common_database), os.path.join(root, "update.sql"))
        pbar.set_description(sql_file)
