#!/usr/bin/env python
'''
WSGI.py
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))
COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True,include=basedir + '/ooiservices/app/*')
    COV.start()
from ooiservices.app import create_app, db
from flask.ext.script import Manager, Shell, Server, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand
import flask.ext.whooshalchemy as whooshalchemy
from ooiservices.app.models import PlatformDeployment, User, UserScope, UserScopeLink
from datetime import datetime

import yaml
if os.path.exists(os.path.join(basedir, '/ooiservices/app/config_local.yml')):
    with open(basedir + '/ooiservices/app/config_local.yml', 'r') as f:
        doc = yaml.load(f)
else:
    with open(basedir + '/ooiservices/app/config.yml', 'r') as f:
        doc = yaml.load(f)
env = doc['ENV_NAME']

app = create_app(env)
manager = Manager(app)
migrate = Migrate(app,db)
app.config['WHOOSH_BASE'] = 'ooiservices/whoosh_index'
whooshalchemy.whoosh_index(app, PlatformDeployment)

if __name__ == '__main__':
    app.run(host='localhost:4001', debug=True)
