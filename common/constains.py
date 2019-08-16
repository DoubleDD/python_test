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


class richtext:
    __base_fastdfs = '/richtext/fastdfs'
    __base_oss = '/richtext/oss'
    fastdfs = build_url(__base_fastdfs)
    oss = build_url(__base_oss)
    streamFastdfs = build_url(__base_fastdfs+'/stream')
    streamOss = build_url(__base_oss+'/stream')
    downloadFastdfs = build_url(__base_fastdfs+'/download')
    downloadOss = build_url(__base_oss+'/download')
    cropperFastdfs = build_url(__base_fastdfs+'/cropper')
    cropperOss = build_url(__base_oss+'/cropper')
    simpleFastdfs = build_url(__base_fastdfs+'/simple')
    simpleAuthFastdfs = build_url(__base_fastdfs+'/simple-auth')
    simpleOss = build_url(__base_oss + '/simple')
    simpleAuthOss = build_url(__base_oss + '/simple-auth')
