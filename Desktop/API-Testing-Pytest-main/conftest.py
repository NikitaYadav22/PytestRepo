from datetime import datetime
import re
import pytest
from py.xml import html
import itertools


@pytest.mark.optionalhook
def pytest_reporter_context(context, config):
	context["title"] = "GRUBHUB"




# # @pytest.hookimpl(trylast=True)
# # def pytest_configure(config):
# #     allure.environment(test_server='testserver', report='My Test Report')

# def pytest_html_results_table_header(cells):
#     cells.insert(0, html.td("Time", class_="sortable time", col="time"))
#     cells.insert(1, html.th("Tag"))
#     cells.insert(2, html.th("Testcase"))
#     cells.pop()

# def pytest_html_results_table_row(report, cells):
#     ''' orienting the data gotten from  pytest_runtest_makereport 
#     and sending it as row to the result '''
#     del cells[1]
#     cells.insert(0, html.td(datetime.utcnow(), class_='col-time'))
#     cells.insert(1, html.td(report.tag))
#     cells.insert(2, html.td(report.testcase))
#     cells.pop()
    
    
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''data from the output of pytest gets processed here
#      and are passed to pytest_html_results_table_row'''
#     outcome = yield
#     # this is the output that is seen end of test case
#     report = outcome.get_result()
#     # taking doc string of the string
#     testcase = str(item.function.__doc__)
#     # name of the functton
#     c = str(item.function.__name__)[5:]
    
#     report.testcase = f"{c} [{testcase}]"
#     # taking input args
#     # example:
#     #      report.nodeid = 'tests/test_case.py::test_min[input0-1]'
#     #    data = re.split(r"\[|\]", 'tests/test_case.py::test_min[input0-1]')
#     #    =>  ['tests/test_case.py::test_min', 'input0-1', '']
#     report.tag= re.split(r"\[|\]", report.nodeid)[-2]

    

  
    