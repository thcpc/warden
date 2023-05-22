from diff_report_1_0_0.accordion_col import AccordionCol
from diff_report_1_0_0.p_tag import PTag


class AccordionItem:
    def __init__(self, left_table, right_table, compare, compare_results: list[dict]):
        self.left_table = left_table
        self.right_table = right_table
        self.css_clazz = "" if compare == 'eql' else "diff"
        self.left_col = self.init_left_cols(compare_results)
        self.right_col = self.init_right_cols(compare_results)

    def init_left_cols(self, compare_results: list[dict]):
        col = AccordionCol(self.left_table)
        for compare_result in compare_results:
            for i in compare_result.get('left'):
                col.add_tag(PTag(i, compare_result.get('marked')))
        return col

    def init_right_cols(self, compare_results: list[dict]):
        col = AccordionCol(self.right_table)
        for compare_result in compare_results:
            for i in compare_result.get('right'):
                col.add_tag(PTag(i, compare_result.get('marked')))
        return col
