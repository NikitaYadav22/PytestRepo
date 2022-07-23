from unittest import TestSuite
from setuptools import setup, find_packages

setup(
    name='My First Setup File',
    version='1.1',
    packages=find_packages(),
     package_data={'pytest_reporter_html1': ['templates/html1/*']},
    include_package_data=True,
    test_suite='Tests.test',
    entry_points={
        'pytest11': [
            'reporter_html1 = pytest_reporter_html1.plugin',
        ]
    }
)
