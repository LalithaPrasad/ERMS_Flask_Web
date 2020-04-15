import os
from datetime import datetime,timedelta
from app_package import db
from werkzeug import generate_password_hash, check_password_hash

class Admin(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), unique=True)
    password_hash=db.Column(db.String(128))
    token=db.Column(db.String(128))
    token_expiry=db.Column(db.DateTime)

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def get_token(self):
        self.token=os.urandom(3).hex()
        self.token_expiry=datetime.utcnow()+timedelta(seconds=360)
        db.session.commit()
        return self.token

    def valid_token(self):
        return (datetime.utcnow()+timedelta(seconds=60))<self.token_expiry

class Employee(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64))
    age=db.Column(db.Integer)
    ed=db.Column(db.String(64))
    role=db.Column(db.String(64))
