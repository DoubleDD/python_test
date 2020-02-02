# -*- coding:utf-8 -*-
import init_env
import redis

env = {
    'rasdev': {
        'host': '121.199.58.186',
        'port': 31306,
        'password': 'TA6sMiuSRqtTrHB7Amdg'
    },
    'local': {
        'host': '127.0.0.1',
        'port': 6379,
        'password': None
    }
}


config = env['rasdev']
r = redis.Redis(host=config['host'],
                port=config['port'],
                password=config['password'])
prefix = 'course-study-async-service#resource-progress-sync'

RESOURCE_PROGRESS_KEYS=f'{prefix}#resource-progress-keys'
keys = r.get(RESOURCE_PROGRESS_KEYS)
print(keys.decode('utf8'))


# test
config = env['local']
r = redis.Redis(host=config['host'],
                port=config['port'],
                password=config['password'])

r.set('root', 'admin')

print(r.get('root').decode('utf8'))
