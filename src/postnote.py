import flask

from flask import render_template, redirect, session
from flask_cors import cross_origin

# Create the flask application object.
app = flask.Flask(__name__)

# Postnote site index.
@app.route('/', methods=['GET'])
def index():
    # Render the Postnote index template.
    return render_template('index.html')

# Login to the Postnote service.
@app.route('/login', methods=['GET'])
def login():
    if 'email' in session:
        return redirect('/dashboard')
    else:
        return redirect('/')

# Post message route.
@app.route('/<user>/post', methods=['GET', 'POST'])
@cross_origin()
def post(user):
    if 'email' in session:
        return render_template('welcome')
    return redirect('/')


if __name__ == '__main__':
    app.run(port=8097, debug=True)
