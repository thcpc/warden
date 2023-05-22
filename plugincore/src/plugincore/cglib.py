import pkg_resources


class Cglib:
    # @staticmethod
    # def plugin_factory(plugin):
    #     return plugin_factory(plugin.id, plugin.version)
    #     # for entry_point in pkg_resources.iter_entry_points(f'{plugin.id}_{plugin.version}.plugin'):
    #     #     return entry_point.load()()

    @staticmethod
    def plugin_factory(plugin_id, plugin_version):
        for entry_point in pkg_resources.iter_entry_points(f'{plugin_id}_{plugin_version}.plugin'):
            return entry_point.load()()
