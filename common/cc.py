# -*- coding:utf-8 -*-

URL_API = "http://localhost:8888/api/v1/content"
URL_AUTH = 'https://dev9.zhixueyun.com/oauth/api/v1/auth'


def build_url(url):
    return URL_API+url


class company_config:
    url = '/company-config'
    callbackConfig = build_url(url+'/login-config')

