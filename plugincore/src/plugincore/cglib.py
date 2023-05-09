import pkg_resources

# from plugin import Plugin


def plugin_factory(plugin):
    for entry_point in pkg_resources.iter_entry_points(f'{plugin.id}_{plugin.version}.plugin'):
        return entry_point.load()()

