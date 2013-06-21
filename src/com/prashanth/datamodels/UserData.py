from google.appengine.ext import db


class UserData(db.Model):
    name = db.StringProperty()
    gender = db.StringProperty()
    age = db.IntegerProperty()
    
class MovieDetails(db.Model):
    movieName = db.StringProperty(multiline=True)
    movieImage = db.StringProperty(multiline=True)
    movieLink = db.StringProperty(multiline=True)
    movieYear = db.IntegerProperty()
    movieTrendingCount = db.IntegerProperty()

