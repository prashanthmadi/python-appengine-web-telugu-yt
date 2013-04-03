from google.appengine.ext import db


class UserData(db.Model):
    name = db.StringProperty()
    gender = db.StringProperty()
    age = db.IntegerProperty()
    
