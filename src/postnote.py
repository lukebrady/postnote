import flask

from flask import render_template, request, redirect, session

# Create the flask application object.
app = flask.Flask(__name__)

# Postnote site index.
@app.route('/', methods=['GET'])
def index():
    # Render the Postnote index template.
    return render_template('index.html')

# Post message route.
@app.route('/post', methods=['GET', 'POST'])
def post():
    if 'email' in session:
        return render_template('welcome')
    return render_template('index')


if __name__ == '__main__':
    app.run(port = 8097, debug=True)

