# -*- coding:utf-8 -*-
import init_env

from common.env_config import ServerCC
from common.login import getToken


server = ServerCC()
# env = ServerCC.LOCAL
env = ServerCC.RASDEV
# env = ServerCC.TEST


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
    return server.getEnv(env)[0] + url
