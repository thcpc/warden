import os
import yaml
import cglib


class Plugin:
    def __init__(self, abs_path):
        with open(os.path.join(abs_path, 'plugin.yaml'), encoding='utf-8') as f:
            self.config = yaml.safe_load(f.read())

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
        return self.config.get("before_plugins", [])

    @property
    def version(self):
        return self.required_property("version")

    def _run_before(self, *args, **kwargs):
        for plugin in self.before_plugins:
            cglib.plugin_factory(plugin).run(*args, **kwargs)

    def _run_after(self, *args, **kwargs):
        for plugin in self.after_plugins:
            cglib.plugin_factory(plugin).run(*args, **kwargs)

    """
    需覆写
    """
    def task(self, *args, **kwargs): ...

    """
    需覆写
    """
    def finalize(self): ...

    def run(self, *args, **kwargs):
        self._run_before(*args, **kwargs)
        self.task(*args, **kwargs)
        self._run_after(*args, **kwargs)
        self.finalize()
