from plugincore import Plugin


class PluginForm:
    def __init__(self, plugin: Plugin, form_data: dict):
        self.form_data = form_data.get(plugin.id)