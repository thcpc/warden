import os.path

from jinja2 import Environment, FileSystemLoader

from diff_report_lib_1_0_0._plugin_args import _PluginArgs
from diff_report_lib_1_0_0.html.accordion_item import AccordionItem


class HtmlFactory:
    def __init__(self, plugin_args: _PluginArgs):
        self.plugin_args = plugin_args

    def gen(self, running_env="dev") -> str:
        env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "../resources")))
        template = env.get_template(os.path.join(f"{running_env}.html"))
        html = f'{self.plugin_args.task_id}.html'
        with open(html, "w+", encoding="utf-8") as f:
            html_content = template.render(
                accordion_items=[self.gen_accordion_item(item) for item in self.plugin_args.compare_data],
                title=self.plugin_args.title,
                left=self.plugin_args.left,
                right=self.plugin_args.right,
                running_env=running_env,
                allCount=len(self.plugin_args.compare_data),
                sameCount=len(list(filter(lambda x: x.get("compare") == 'eql', self.plugin_args.compare_data))),
                diffCount=len(list(filter(lambda x: x.get("compare") == 'diff', self.plugin_args.compare_data))))
            f.write(html_content)
        return html

    def gen_accordion_item(self, item):
        return AccordionItem(item.get("leftName"), item.get("rightName"), item.get("compare"),
                             item.get(item.get("compare")))

