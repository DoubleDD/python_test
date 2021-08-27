import init_env

yunli_env = 'dev'

server = {
    'dev': 'http://39.100.95.69:30102',
    'prod': 'http://60.13.54.71:30118'
}

def getServer(env=None) -> str:
    if env is None:
        env = yunli_env
    return server[env]



class Api:
    heartbeat = getServer()+'/yunli/portal/v1/api/global/heartbeat'
