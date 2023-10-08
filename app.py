from flask import Flask, render_template, redirect, url_for, request
from config import app,db,Fixtures


with app.app_context():
    db.create_all()
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/standings')
def standings():
    return render_template('standings.html')

@app.route('/fixtures')
def fixtures():
    fixtures = Fixtures(time="14:00",day_month="Friday Oct",date="05/10/23",team_1="New Zealand",team_2="England",venue="Narendra Modi Staduium",matchNumber="1")
    db.session.add(fixtures)
    db.session.commit()
    return render_template('fixtures.html')

@app.route('/Fan_Poll')
def Fan_Poll():
    return render_template('Fan_Poll.html')

if __name__ == "__main__":
    app.run(debug=True)