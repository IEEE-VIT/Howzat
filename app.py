from flask import Flask, render_template, redirect, url_for, request
from config import app,db


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
    return render_template('fixtures.html')

@app.route('/Fan_Poll')
def Fan_Poll():
    return render_template('Fan_Poll.html')

if __name__ == "__main__":
    app.run(debug=True)
    