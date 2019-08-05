# -*- coding:utf-8 -*-

URL_API = "http://localhost:10092/api/v1/file"
URL_AUTH = 'https://dev9.zhixueyun.com/oauth/api/v1/auth'


def build_url(url):
    return URL_API+url


class index:
    fastdfsTest = build_url('/fastdfs/test')
    ossTest = build_url('/oss/test')
    image = build_url('/image/test')


class info:
    get = build_url("/attachment")


class base64Upload:
    fastdfs = build_url('/upload-base64/fastdfs')
    oss = build_url('/upload-base64/oss')
