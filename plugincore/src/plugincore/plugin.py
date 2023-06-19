import os
import yaml
from cjen.nene.properties import required

from plugincore.exceptions.plugin_fail_err import PluginFailErr
from plugincore.exceptions.plugin_property_err import PluginPropertyErr
from plugincore.exceptions.plugin_running_args_err import PluginRunningArgsErr
from plugincore.plugin_run_audit import PluginRunAudit
from plugincore.cglib import Cglib
from plugincore.plugin_run_record import PluginRunRecord
from plugincore.properties.processor_property import ProcessorProperty


class Plugin:
    def __init__(self, abs_path):
        with open(os.path.join(abs_path, 'plugin.yaml'), encoding='utf-8') as f:
            self.config = yaml.safe_load(f.read())
        self.plugin_run_audit = PluginRunAudit()
        self.step_count = 0

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
    def pre_processors(self) -> list:
        if not self.config.get("pre_processors"): return []
        return [ProcessorProperty(meta) for meta in self.config.get("pre_processors")]

    @property
    def post_processors(self) -> list:
        if not self.config.get("post_processors"): return []
        return [ProcessorProperty(meta) for meta in self.config.get("post_processors")]

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

    def _run_pre_processors(self, form_data: dict):
        for processor in self.pre_processors:
            audit = Cglib.plugin_factory(processor.plugin_id, processor.version).run(form_data)
            audit << {"processor": processor.name}
            self.plugin_run_audit.append(audit)
            if not self.plugin_run_audit.ok: break

    def _run_post_processors(self, form_data: dict):
        for processor in self.post_processors:
            audit = Cglib.plugin_factory(processor.plugin_id, processor.version).run(form_data)
            audit << {"processor": processor.name}
            self.plugin_run_audit.append(audit)
            if not self.plugin_run_audit.ok: break

    """
    需覆写
    """

    def processor(self, form_data: dict):
        ...

    def before(self, form_data: dict):
        ...

    def after(self, form_data: dict):
        ...

    """
    需覆写
    """

    def finalize(self, form_data: dict):
        ...

    def run(self, form_data: dict, need_estimate: bool = False):
        try:
            if need_estimate:
                self.total_estimate(form_data)
            for callee in [self._run_pre_processors,
                           self.before,
                           self.processor,
                           self.after,
                           self._run_post_processors,
                           self.finalize]:
                if self.plugin_run_audit.ok:
                    callee(form_data)
            self.audit(dict(status=200, msg=f"{self.id} success"))
        except (PluginFailErr, PluginPropertyErr, PluginRunningArgsErr) as e:
            self.audit(e())

        return self.plugin_run_audit

    def total_estimate(self, form_data) -> int:

        if self.step_count == 0:
            for processor in self.pre_processors + self.post_processors:
                self.step_count += Cglib.plugin_factory(processor.plugin_id, processor.version).estimate(
                    form_data)
            self.step_count += self.estimate(form_data)
        return self.step_count

    def estimate(self, form_data) -> int:
        return 1

    def progress(self):
        ...
