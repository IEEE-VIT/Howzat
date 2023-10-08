from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Create a Flask Instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#Initialize Database
db = SQLAlchemy(app)
    
class Fixtures(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    time=db.Column(db.String(5))
    day_month=db.Column(db.String(10))
    date=db.Column(db.String(100))
    team_1=db.Column(db.String(200),nullable=False)
    team_2=db.Column(db.String(200),nullable=False)
    venue=db.Column(db.String(200))
    matchNumber=db.Column(db.String(3),nullable=False)
    
    def __repr__ (self):
        return '<matchNumber %r>' % self.venue