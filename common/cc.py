# -*- coding:utf-8 -*-
from init_env import BASE_DIR
from common.env_config import ServerCC

env = ServerCC.DEV
URL_AUTH = 'https://dev9.zhixueyun.com/oauth/api/v1/auth'


def build_url(url):
    server = ServerCC()
    return server.getEnv(env)[0] + "/api/v1/content" + url


class company_config:
    url = '/company-config'
    CALLBACK_CONFIG = build_url(url+'/login-config')


class company_resource:
    url = '/company-resources'
    LIST = build_url(url + '/list')
    GRANT_RESOURCE_PROVIDER = build_url(url+'/grant/resource-provider')


class Order:
    url = '/order'
    LIST = build_url(url+'/list')
    DETAIL = build_url(url+'/detail/')
