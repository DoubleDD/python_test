# -*- coding:utf-8 -*-
import unittest


def runTests(tests=None):
    suit = unittest.TestSuite()
    if tests is None:
        return
    for test in tests:
        suit.addTest(test)
    runner = unittest.TextTestRunner()
    runner.run(suit)
