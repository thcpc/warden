from cjen.nene.properties import required

from plugincore.exceptions.plugin_property_err import PluginPropertyErr


class ProcessorProperty:
    def __init__(self, meta: dict):
        self.meta = meta

    @property
    @required(exception_class=PluginPropertyErr, err_msg='Plugin id is Required')
    def processor(self): return self.meta.get("processor")

    @property
    @required(exception_class=PluginPropertyErr, err_msg='Plugin id is Required')
    def plugin_id(self): return self.meta.get("plugin_id")

    @property
    @required(exception_class=PluginPropertyErr, err_msg='Plugin id is Required')
    def version(self): return self.meta.get("version")
