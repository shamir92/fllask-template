import os

class Config(object):
    # App default config
    APP_ENV = os.environ.get('APP_ENV',"localhost")
    APP_DEBUG = os.environ.get("APP_DEBUG", False)
    APP_PORT = os.environ.get("APP_PORT",5000)
