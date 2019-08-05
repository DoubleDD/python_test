# -*- coding:utf-8 -*-
import init_env
from common.HttpUtils import HttpUtils
from common.constains import info
from test_cases.base_test import runTests
import unittest


class TestAttachmentInfo(unittest.TestCase):
    def setUp(self):
        self.r = HttpUtils()
        pass

    def tearDown(self):
        pass

    def test_get(self):
        id = '20822da6-2c51-45b7-b88c-1c6c5b3749a2'
        response = self.r.get(info.get+'/'+id)
        self.r.logJson(jsonObj=response.json())

    def addTest(self, suit):
        suit.addTest()
        return suit


if __name__ == "__main__":
    tests = [
        TestAttachmentInfo('test_get')
    ]
    runTests(tests)
