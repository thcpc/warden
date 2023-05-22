import importlib
from plugincore.cglib import Cglib
from flask import Blueprint, render_template, request

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route('/')
def index():
    return render_template('main/index.html', task_cards=user_settings())


@bp.route('/submit_task', methods=['POST'])
def submit_task():
    form = request.form


def user_settings() -> list[dict]:
    plugins = [dict(id="db_compare", version="1_0_0")]
    plugin_cards = []
    for plugin in plugins:
        card = Cglib.plugin_factory(plugin.get("id"), plugin.get("version"))
        plugin_cards.append(dict(name=card.name, description=card.description, id=card.id, home=card.home))
    return plugin_cards
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
