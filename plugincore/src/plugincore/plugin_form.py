from plugincore import Plugin
from plugincore.exceptions.plugin_running_args_err import PluginRunningArgsErr


class PluginForm:
    def __init__(self, plugin: Plugin, form_data: dict):
        self.plugin = plugin
        self._data = form_data

    @property
    def form_data(self):
        if self._data.get(self.plugin.id) is None: raise PluginRunningArgsErr(f'{self.plugin.id} need form_data')
        return self._data.get(self.plugin.id)

    @property
    def task_id(self):
        if self.form_data.get("task_id") is None: raise PluginRunningArgsErr(f'{self.plugin.id} form_data need task_id')
        return self.form_data.get("task_id")
