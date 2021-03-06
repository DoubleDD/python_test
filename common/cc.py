# -*- coding:utf-8 -*-
import init_env

from common.env_config import ServerCC
from common.login import getToken

server = ServerCC()
env = ServerCC.RASDEV


def get_token():
    data = {
        'key': 'oZImo5zozQggF2BymfTc090trJ3N6xyWfo18/8Lp7jTh8l2v5iCDg5phuOMsAthCWpnEJqsiMBtxMaMJ+1oBvaY4o9ONCHnNuQ636V9wYD3lmnYIQHqt4yWVTPKgmBySaQToc6WyGn/ZQzVCfTb/ZHbE9n1fYt0vYI4VFwXKaTA6Tat8KQgvApOL69rDME2r0039DIBeJco3Us0l2I422FpNXnwkg0YZvW25RuSKKJ0=',
        'organization_id': 'JxY2o34iEXLHxVjR9M2JdgcqJIa1LW0a3xHIMm7XpsJAFlAUDoaSMYj6mn+Oy6Nn',
        'login_method': 'JZNm+1f9txtGtiE0oRMJ1g==',
        'username': 'PjDD8fU4asbLJXaEbcNEwg==',
        'pword': '0GrD6MYSpX0BOZW15fev2w==',
        'captcha': ''
    }
    url = server.getEnv(env)[1]
    return getToken(url, data)


def build_url(url):
    return server.getEnv(env)[0] + "/api/v1/content" + url


class CompanyConfig:
    url = '/company-config'
    CALLBACK_CONFIG = build_url(url+'/login-config')


class ResourcePark:
    url = '/resources-park'
    CONFIG_JSON = build_url(url+'/config-json')


class CompanyResource:
    url = '/company-resources'
    LIST = build_url(url + '/list')
    GRANT_RESOURCE_PROVIDER = build_url(url+'/grant/resource-provider')


class Order:
    url = '/order'
    LIST = build_url(url+'/list')
    DETAIL = build_url(url+'/detail/multipart/')


class CourseInfo:
    url = '/course-info'
    AUTH = build_url(url)


class Test:
    url = '/test'
    AUTH = build_url(url+'/auth')


class ConsumerLearningProgress:
    API_KEY = 'e61121d3d39f649c1f847e470abf2e95'
    SECRET_KEY = '9b16400cd267e4c685df447178570ed5'

    url = '/resource/learning/progress'
    course = build_url(url+'/course')
    external_activity = build_url(url+'/external-activity')
    subject = build_url(url+'/subject')


class LearningProgress:
    API_KEY = '4ff60d0c4dfa56476a09d470ad50c715'
    SECRET_KEY = 'f9b2f73b44333a748103f36dac1a7648'

    url = '/resource/learning/progress'
    course = build_url(url+'/course')
    external_activity = build_url(url+'/external-activity')
    subject = build_url(url+'/subject')


class UserInfo:
    url = build_url('/user/info/simple')
