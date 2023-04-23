import importlib


def print_hi(name):
    p = importlib.import_module('db_compare')
    print(p.Plugin().home)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
