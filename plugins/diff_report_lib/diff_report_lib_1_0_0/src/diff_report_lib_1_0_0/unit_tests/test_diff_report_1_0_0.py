from diff_report_lib_1_0_0.diff_report_lib_plugin import DiffReportLibPlugin
from diff_report_lib_1_0_0.unit_tests.TestData import test_data


def test_plugin_run():
    diff_report = DiffReportLibPlugin()
    comare_data = dict(task_id=11111, title="测试", left="xxxxxx", right="ddddddd", compare_data=test_data)
    diff_report.run(DiffReportPlugin=comare_data)
