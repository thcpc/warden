class PluginPropertyErr(Exception):
    def __init__(self, *args, **kwargs):
        self.err = args[0]

    def __call__(self, *args, **kwargs): return dict(status=-100, err=self.err)