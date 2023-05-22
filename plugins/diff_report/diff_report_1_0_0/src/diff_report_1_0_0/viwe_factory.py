import os.path

from jinja2 import Environment, FileSystemLoader


from diff_report_1_0_0.accordion_item import AccordionItem


class ViewFactory:
    def __init__(self, compare_data: list):
        self.compare_data = compare_data

    def gen(self, version: int, system: str, release_type: str) ->str:
        env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "resources")))
        template = env.get_template(os.path.join("report.templte.html"))
        html = f'{system}_{release_type}_V{str(version)}.html'
        with open(html, "w+", encoding="utf-8") as f:
            html_content = template.render(accordion_items=[self.gen_accordion_item(item) for item in self.compare_data],
                                           Version=version, System=system)
            f.write(html_content)
        return html

    def gen_accordion_item(self, item):
        return AccordionItem(item.get("leftName"), item.get("rightName"), item.get("compare"), item.get(item.get("compare")))

#
# if __name__ == '__main__':
#     db1 = DataBaseDLL("design_incremental_sql")
#     db1.load()
#     db2 = DataBaseDLL("design_initial_sql")
#     db2.load()
#     ct = CompareTask(db1, db2)
#     ct.run()
#     ViewFactory(ct.result).gen()
