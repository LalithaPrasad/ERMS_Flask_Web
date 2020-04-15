from functools import wraps
from flask import session,flash,redirect,url_for
from app_package.models import Admin

def valid_token(func):
    @wraps(func)
    def inner(*args,**kwargs):
        admin=Admin.query.get(1)
        token=session.get("token") or None
        if (admin and admin.token==token and admin.valid_token()):
            return func(*args,**kwargs)
        else:
            flash("Invalid token")
            return redirect(url_for("logout"))
    return inner
