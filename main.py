# -*- coding:utf-8 -*-
import HtmlTestRunner
import unittest
import init_env
from common.DateUtils import DateTimeFormat


# test_dir = init_env.BASE_DIR+'\\test_cases'
test_dir = './test_cases'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')


if __name__ == "__main__":
    output_dir = '测试报告/'+DateTimeFormat('%Y-%m-%d_%H-%M-%S')
    runner = HtmlTestRunner.HTMLTestRunner(output=output_dir)
    runner.run(discover)
