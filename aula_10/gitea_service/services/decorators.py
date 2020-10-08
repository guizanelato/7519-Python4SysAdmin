import functools

from flask import session, redirect

def login_required(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if not session.get('auth'):
            return redirect('/sign-in')
        return function(*args, **kwargs)
    return wrapper

