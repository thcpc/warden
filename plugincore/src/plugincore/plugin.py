import os
import yaml

from plugincore.plugin_run_result import PluginRunResult
from plugincore.cglib import Cglib


class Plugin:
    def __init__(self, abs_path):
        with open(os.path.join(abs_path, 'plugin.yaml'), encoding='utf-8') as f:
            self.config = yaml.safe_load(f.read())
        self.plugin_run_result = PluginRunResult()

    def required_property(self, key):
        if self.config.get(key) is None: raise Exception(f'Plugin {key} is Required')
        return self.config.get(key)

    @property
    def id(self):
        return self.required_property("id")

    @property
    def name(self):
        return self.required_property("name")

    @property
    def description(self):
        return self.required_property("description")

    @property
    def before_plugins(self):
        return self.config.get("before_plugins", [])

    @property
    def after_plugins(self):
        return self.config.get("after_plugins", [])

    @property
    def version(self):
        return self.required_property("version")

    def _run_before(self, *args, **kwargs):
        for plugin in self.before_plugins:
            self.plugin_run_result.append(Cglib.plugin_factory(plugin.get("plugin_id"), plugin.get("version")).run(*args, **kwargs))
            if not self.plugin_run_result.ok: break

    def _run_after(self, *args, **kwargs):
        for plugin in self.after_plugins:
            self.plugin_run_result.append(Cglib.plugin_factory(plugin.get("plugin_id"), plugin.get("version")).run(*args, **kwargs))
            if not self.plugin_run_result.ok: break

    """
    需覆写
    """

    def task(self, *args, **kwargs):
        ...

    """
    需覆写
    """

    def finalize(self):
        ...

    def run(self, *args, **kwargs):
        self._run_before(*args, **kwargs)
        if self.plugin_run_result.ok:
            self.task(*args, **kwargs)
        if self.plugin_run_result.ok:
            self._run_after(*args, **kwargs)
        if self.plugin_run_result.ok:
            self.finalize()
        return self.plugin_run_result
