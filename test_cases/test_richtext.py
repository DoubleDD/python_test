# -*- conding:utf-8 -*-
from init_env import BASE_DIR
from common.HttpUtils import HttpUtils
from common.constains import richtext
import unittest
from test_cases.base_test import runTests
from common.login import getToken
from common.ContentType import http


class TestRichtext(unittest.TestCase):
    """富文本编辑器中文件上传接口测试

    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        self.r = HttpUtils()
        self.files = {'file': open(BASE_DIR+'/resouces/stock.jpg', 'rb')}
        self.token = getToken()
        self.contentType = http.text

    def tearDown(self):
        pass

    def test_fastdfs(self):
        result = self.r.post(url=richtext.fastdfs, files=self.files)
        self.r.logJson(jsonStr=result.text)

if __name__ == "__main__":
    runTests([
        TestRichtext('test_fastdfs')
    ])
