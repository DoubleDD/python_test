# -*- coding:utf-8 -*-
import unittest
import HtmlTestRunner
#import init_env
from common.DateUtils import DateTimeFormat


# test_dir = init_env.BASE_DIR+'\\test_cases'
TEST_DIR = './content-custom'
DISCOVER = unittest.defaultTestLoader.discover(TEST_DIR, pattern='test_*.py')


if __name__ == "__main__":
    OUTPUT_DIR = '测试报告/'+DateTimeFormat('%Y-%m-%d_%H-%M-%S')
    RUNNER = HtmlTestRunner.HTMLTestRunner(output=OUTPUT_DIR)
    RUNNER.run(DISCOVER)
