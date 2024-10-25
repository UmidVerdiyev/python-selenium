import os

class AllureReportUtil:
    allure_results_dir = "allure-results"

    @staticmethod
    def setup_report_directory():

        if not os.path.exists(AllureReportUtil.allure_results_dir):
            os.makedirs(AllureReportUtil.allure_results_dir)

    @staticmethod
    def get_results_path():
        AllureReportUtil.setup_report_directory()
        return AllureReportUtil.allure_results_dir
