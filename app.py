from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from populate import populate
import config
import functools

app = config.app

with app.app_context():
    populate(config)

# storing the user details in session after Authentication.
session = {}

# decorator to redirect the use to login.html page
def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return secure_function
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/standings')
def standings():
    return render_template('standings.html')

@app.route('/fixtures')
def fixtures():
    return render_template('fixtures.html')

@app.route('/Fan_Poll')
@login_required
def Fan_Poll():
    return render_template('Fan_Poll.html', username=session["username"])

if __name__ == "__main__":
    app.run(debug=True)
    