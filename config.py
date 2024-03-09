import os

class Config(object):
    # App default config
    APP_ENV = os.environ.get('APP_ENV',"localhost")
    APP_DEBUG = os.environ.get("APP_DEBUG", False)
    APP_PORT = os.environ.get("APP_PORT",5000)


    ## for db
    SQLALCHEMY_DATABASE_URI = "mysql://{user}:{pw}@{url}/{db}".format(
        user=os.environ.get("DB_USER","root"),
        pw=os.environ.get("DB_PASSWORD","root"),
        url=os.environ.get("DB_URL","localhost:3306"),
        db=os.environ.get("DB_DATABASE","db" ),
    )
    SQLALCHEMY_ECHO=os.environ.get("SQLALCHEMY_ECHO", False)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
