"""
    guestbookapp.models
    ===================

"""
from google.appengine.ext import db

class Message(db.Model):
    text = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now=True)