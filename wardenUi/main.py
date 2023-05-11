import importlib
from flask import Blueprint, render_template
bp = Blueprint("main", __name__, url_prefix="/")


@bp.route('/')
def index():
    return render_template('main/index.html', task_cards=user_settings())


def user_settings() -> list[dict]:
    tasks_cards = [dict(id="tsc",
                        name="表结构对比",
                        description="数据库结构比对工具，主要用来比对指定的两个 schema 的结构是否一致")]
    return tasks_cards
# import pkg_resources
#
#
# def print_hi(name):
#     for entry_point in pkg_resources.iter_entry_points('db_compare.plugin'):
#         plugin = entry_point.load()()
#         plugin.home
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
