# -*- coding:utf-8 -*-
import init_env
from common.HttpUtils import HttpUtils
from common.constains import URL_API
import os


def test():
    r = HttpUtils()
    result = r.get(URL_API)
    print(result.text)


if __name__ == "__main__":
    test()
    file = open('./resouces/stock-photo-166606087.jpg', 'rb')
    info = os.path.splitext(file.name)
    print(info)
