from flask import render_template
from populate import populate
import config

app = config.app

with app.app_context():
    populate(config)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/standings')
def standings():
    return render_template('standings.html')

@app.route('/fixtures')
def fixtures():
    fixtures = config.Fixtures.query.all()
    return render_template('fixtures.html', fixtures=fixtures)

@app.route('/Fan_Poll')
def Fan_Poll():
    return render_template('Fan_Poll.html')

if __name__ == "__main__":
    app.run(debug=True)
    