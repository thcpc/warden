from plugincore.plugin_form import PluginForm


class DiffReportLibPluginForm(PluginForm):

    @property
    def task_id(self): return self.form_data.get("task_id")

    @property
    def left(self): return self.form_data.get("left")

    @property
    def right(self): return self.form_data.get("right")

    @property
    def compare_data(self): return self.form_data.get("compare_data")

    @property
    def title(self): return self.form_data.get("title")
