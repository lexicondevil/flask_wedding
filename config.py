#!/Users/rmcdonough/Envs/semi/bin/python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

CSRF_ENABLED = True
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
TESTING = False
