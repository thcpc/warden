from diff_report_1_0_0.diff_report_plugin import DiffReportPlugin
from diff_report_1_0_0.unit_tests.TestData import test_data


def test_plugin_run():
    diff_report = DiffReportPlugin()
    comare_data = dict(title="测试", left="xxxxxx", right="ddddddd", compare_data=test_data)
    diff_report.run(DiffReportPlugin=comare_data)
