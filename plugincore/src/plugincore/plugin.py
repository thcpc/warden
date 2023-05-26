import os
import yaml
from cjen.nene.properties import required

from plugincore.exceptions.plugin_fail_err import PluginFailErr
from plugincore.exceptions.plugin_property_err import PluginPropertyErr
from plugincore.plugin_run_audit import PluginRunAudit
from plugincore.cglib import Cglib
from plugincore.plugin_run_record import PluginRunRecord


class Plugin:
    def __init__(self, abs_path):
        with open(os.path.join(abs_path, 'plugin.yaml'), encoding='utf-8') as f:
            self.config = yaml.safe_load(f.read())
        self.plugin_run_audit = PluginRunAudit()

    # def required_property(self, key):
    #     if self.config.get(key) is None: raise Exception(f'Plugin {key} is Required')
    #     return self.config.get(key)

    @property
    @required(exception_class=PluginPropertyErr, err_msg='Plugin id is Required')
    def id(self):
        return self.config.get("id")

    @property
    @required(exception_class=PluginPropertyErr, err_msg='Plugin name is Required')
    def name(self):
        return self.config.get("name")

    @property
    @required(exception_class=PluginPropertyErr, err_msg='Plugin description is Required')
    def description(self):
        return self.config.get("description")

    @property
    def before_plugins(self):
        return self.config.get("before_plugins", [])

    @property
    def after_plugins(self):
        return self.config.get("after_plugins", [])

    @property
    @required(exception_class=PluginPropertyErr, err_msg='Plugin version is Required')
    def version(self):
        return self.config.get("version")

    def audit(self, content):
        try:
            record = PluginRunRecord() << content << {"plugin.id": self.id, "plugin.version": self.version}
        except PluginPropertyErr as e:
            record = PluginRunRecord() << e()
        self.plugin_run_audit.add(record)

    def _run_before(self, form_data: dict):
        for plugin in self.before_plugins:
            self.plugin_run_audit.append(
                Cglib.plugin_factory(plugin.get("plugin_id"), plugin.get("version")).run(form_data))
            if not self.plugin_run_audit.ok: break

    def _run_after(self, form_data: dict):
        for plugin in self.after_plugins:
            self.plugin_run_audit.append(
                Cglib.plugin_factory(plugin.get("plugin_id"), plugin.get("version")).run(form_data))
            if not self.plugin_run_audit.ok: break

    """
    需覆写
    """

    def task(self, form_data: dict):
        ...

    """
    需覆写
    """

    def finalize(self):
        ...

    def run(self, kwargs: dict):
        try:
            self._run_before(kwargs)
            if self.plugin_run_audit.ok:
                self.task(kwargs)
            if self.plugin_run_audit.ok:
                self._run_after(kwargs)
            if self.plugin_run_audit.ok:
                self.finalize()
        except (PluginFailErr, PluginPropertyErr) as e:
            self.audit(e())
        # except PluginPropertyErr as e:
        #     self.audit(e())
        return self.plugin_run_audit
