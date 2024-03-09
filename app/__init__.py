# from authlib.integrations.flask_client import OAuth
import os
import sys
from flask import Flask, got_request_exception, abort as original_flask_abort
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_sieve import Sieve
from logging.config import dictConfig

# Create package object.
db = SQLAlchemy()
api = Api()
sieve = Sieve()

# Initialize the package that needed
def init_app(name, config=None):
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://flask.logging.wsgi_errors_stream",
                    "formatter": "default",
                },
                "file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "default",
                    "filename": "storage/logs/log.log",
                    "mode": "a",
                    "maxBytes": 1048576,
                    "backupCount": 10,
                },
            },
            "root": {"level": "INFO", "handlers": ["file", "wsgi"]},
        }
    )
    app = Flask(name)
    app.config.from_object(config)
    # db.init_app(app)
    api.init_app(app)
    CORS(app)
    sieve.init_app(app)
    
    return app