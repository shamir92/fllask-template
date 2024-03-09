import os

class Config(object):
    # App default config
    DOMAIN_URL = os.environ.get("DOMAIN_URL")
    APP_ENV = os.environ.get('APP_ENV',"localhost")
    APP_DEBUG = os.environ.get("APP_DEBUG", False)
    APP_PORT = os.environ.get("APP_PORT")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_EXPIRE_TIME = os.environ.get("JWT_EXPIRE_TIME")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SECURITY_PASSWORD_HASH = os.environ.get("SECURITY_PASSWORD_HASH")
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT")
    SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = os.environ.get(
        "SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS"
    )
    WTF_CSRF_ENABLED = os.environ.get("WTF_CSRF_ENABLED")
    WTF_CSRF_CHECK_DEFAULT = os.environ.get("WTF_CSRF_CHECK_DEFAULT")
    WTF_CSRF_METHODS = os.environ.get("WTF_CSRF_METHODS")