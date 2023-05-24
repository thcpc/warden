import difflib

from db_compare_1_0_0.compare.compare_result import CompareResult
from db_compare_1_0_0.schema import Schema


def sub_array(array: list, startx, endx):
    return [array[i] for i in range(startx, endx)]


class CompareTask:
    def __init__(self, left: Schema, right: Schema):
        self.left = left
        self.right = right
        self.size_of_left = len(self.left.tables())
        self.size_of_right = len(self.right.tables())
        self.result = []

    def compare_diff(self, left: list[str], right: list[str]):
        ret = {"diff": []}
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, left, right).get_opcodes():
            ret["diff"].append(CompareResult.create(tag, sub_array(left, i1, i2), sub_array(right, j1, j2)).dict())
            # ret["diff"].append(CompareResult(tag, sub_array(left, i1, i2), sub_array(right, j1, j2)))
        return ret

    def run(self):
        """
               对于表单名比较
               "equal": 不增加
              "insert": 左边增加
               "delete": 右边增加
               "replace":左右都增加
               对于表内容
               "equal": 不增加
              "insert": 左边增加
               "delete": 右边增加
               "replace":不增加

               :return:
               """
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, self.left.tables(), self.right.tables()).get_opcodes():
            if tag == "equal":
                offset = 0
                while offset < i2 - i1:
                    left_ddl = self.left.ddl_of(self.left.get_table_by_index(i1 + offset)).splitlines()
                    right_ddl = self.right.ddl_of(self.right.get_table_by_index(j1 + offset)).splitlines()
                    if self.left.sha1_of(self.left.get_table_by_index(i1 + offset)) != self.right.sha1_of(
                            self.right.get_table_by_index(j1 + offset)):
                        aci = dict(leftName=self.left.get_table_by_index(i1 + offset),
                                   rightName=self.right.get_table_by_index(j1 + offset))
                        aci["compare"] = "diff"
                        aci.update(self.compare_diff(left_ddl, right_ddl))
                        self.result.append(aci)
                        # self.result.append({**{"name": self.left.get_table_by_index(index), "compare": "diff"}, **self.compare_diff(left_ddl, right_ddl)})
                    else:
                        aci = dict(leftName=self.left.get_table_by_index(i1 + offset),
                                   rightName=self.right.get_table_by_index(j1 + offset))
                        aci["compare"] = "eql"
                        aci["eql"] = [CompareResult("equal", left_ddl, right_ddl).dict()]
                        self.result.append(aci)
                        # self.result.append({"name": self.left.get_table_by_index(index), "compare": "eql", "eql": [CompareResult("equal", left_ddl, right_ddl)]})
                    offset += 1
            elif tag == "insert":

                right_ddl = self.right.ddl_of(self.right.get_table_by_index(j1)).splitlines()
                aci = dict(leftName="", rightName=self.right.get_table_by_index(j1))
                aci["compare"] = "diff"
                aci.update(self.compare_diff([], right_ddl))
                self.result.append(aci)
                # self.result.append({**{"name": self.right.get_table_by_index(j1), "compare": "diff"}, **self.compare_diff([], right_ddl)})
            elif tag == "delete":
                left_ddl = self.left.ddl_of(self.left.get_table_by_index(i1)).splitlines()
                aci = dict(leftName=self.left.get_table_by_index(i1), rightName="")
                aci["compare"] = "diff"
                aci.update(self.compare_diff(left_ddl, []))
                self.result.append(aci)
                # self.result.append({**{"name": self.left.get_table_by_index(i1), "compare": "diff"}, **self.compare_diff(left_ddl, [])})
            elif tag == "replace":
                right_ddl = self.right.ddl_of(self.right.get_table_by_index(j1)).splitlines()
                aci = dict(leftName="xxxx", rightName=self.right.get_table_by_index(j1))
                aci["compare"] = "diff"
                aci.update(self.compare_diff([], right_ddl))
                self.result.append(aci)
                # self.result.append({**{"name": self.right.get_table_by_index(j1), "compare": "diff"}, **self.compare_diff([], right_ddl)})
                left_ddl = self.left.ddl_of(self.left.get_table_by_index(i1)).splitlines()
                aci = dict(leftName=self.left.get_table_by_index(i1), rightName="yyyy")
                aci["compare"] = "diff"
                aci.update(self.compare_diff(left_ddl, []))
                self.result.append(aci)
                # self.result.append({**{"name": self.left.get_table_by_index(i1), "compare": "diff"}, **self.compare_diff(left_ddl, [])})
            else:
                pass
