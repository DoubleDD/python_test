# -*- conding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.constains import richtext
import unittest
from test_cases.base_test import runTests
from common.login import getToken
from common.ContentType import http

filename = BASE_DIR+'/resources/stock.jpg'


class TestRichtext(unittest.TestCase):
    """富文本编辑器中文件上传接口测试

    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        self.r = HttpUtils()
        self.files = {'file': open(filename, 'rb')}
        self.token = getToken()
        self.contentType = http.text

    def tearDown(self):
        self.r.logJson(jsonStr=self.result.text)

    def test_fastdfs(self):
        self.result = self.r.post(url=richtext.fastdfs, files=self.files)

    def test_oss(self):
        self.result = self.r.post(url=richtext.oss, files=self.files)

    def test_streamFastdfs(self):
        """流式上传
        """
        with open(filename) as file:
            self.result = self.r.post(url=richtext.streamFastdfs, data=file)


if __name__ == "__main__":
    runTests((
        # TestRichtext('test_fastdfs'),
        # TestRichtext('test_oss'),
        TestRichtext('test_streamFastdfs'),
    ))
