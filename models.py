from . import db
#from this package, we can import anything in init.py
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now()) #func gets the current date and time
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #in sql, foreign key we use lower case

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(60))
  email = db.Column(db.String(150), unique = True)
  password = db.Column(db.String(150), not_null = True)
  first_name = db.Column(db.String(30))
  last_name = db.Column(db.String(30))
  email = db.Column(db.String(50), not_null = True)


class Organizations(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(60))
  email = db.Column(db.String(150), unique = True)
  password = db.Column(db.String(150), not_null = True)
  description = db.Column(db.String(500))
  phoneNum = db.Column(db.Integer)

class events(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  organizerID = db.Column(db.Integer, not_null = True)
  name = db.Column(db.String(60), not_null = True)
  description = db.Column(db.String(500), not_null = True)
  date = db.Column(db.datetime, not_null = True)
  numPositions = db.Column(db.Integer, not_null = True)

class attending(db.Model):
  volunteerIDnum = db.Column(db.Integer, not_null = True)
  eventIDnum = db.Column(db.Integer, not_null = True)

class hosting(db.Model):
  eventIDnum = db.Column(db.Integer, not_null = True)
  orgIDnum = db.Column(db.Integer, not_null = True)

class futureEvents(db.Model):
  volunteerIDnum = db.Column(db.Integer, not_null = True)
  eventIDnum = db.Column(db.Integer, not_null = True)
  date = db.Column(db.datetime, not_null = True)

class pastEvents(db.Model):
  volunteerIDnum = db.Column(db.Integer, not_null = True)
  eventIDnum = db.Column(db.Integer, not_null = True)
  date = db.Column(db.datetime, not_null = True)


