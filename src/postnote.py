import flask

from flask import render_template, redirect, session
from flask_cors import cross_origin
from pndb import PostnoteDB

# Create the flask application object.
app = flask.Flask(__name__)
conn = PostnoteDB(host='192.168.33.40', user='root',passwd='rootpassword1234', database='Postnote')

# Postnote site index.
@app.route('/', methods=['GET'])
def index():
    # Render the Postnote index template.
    return render_template('index.html')

# Login to the Postnote service.
@app.route('/login', methods=['GET'])
def login():
    if 'username' in session:
        return redirect('/dashboard')
    else:
        return render_template('login.html')

# Signup for the Postnote service.
@app.route('/signup', methods=['GET'])
def signup():
    if 'username' in session:
        return redirect('/dashboard')
    else:
        return render_template('signup.html')

# Post message route.
@app.route('/<user>/post', methods=['GET', 'POST'])
@cross_origin()
def post(user):
    if 'username' in session:
        return render_template('welcome')
    return redirect('/')


if __name__ == '__main__':
    app.run(port=8097, debug=True)
