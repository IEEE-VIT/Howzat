from flask import render_template
from populate import populate
from standings_scapper import standings_scapper
import config

SCRAPPING_URL = "https://www.cricketworldcup.com/standings/"

app = config.app

with app.app_context():
    populate(config)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/standings')
def standings():
    standings = standings_scapper(SCRAPPING_URL)
    return render_template('standings.html', standings=standings)

@app.route('/fixtures')
def fixtures():
    fixtures = config.Fixtures.query.all()
    return render_template('fixtures.html', fixtures=fixtures)

@app.route('/Fan_Poll')
def Fan_Poll():
    return render_template('Fan_Poll.html')

if __name__ == "__main__":
    app.run(debug=True)
    