#!/usr/bin/env python
'''
ooiservices.decorators

Custom decorators for OOI services
'''
__author__ = 'M@Campbell'

from functools import wraps
from flask import abort
from flask.ext.login import current_user

def scope_required(scope):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(scope):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator