import flask

from flask import render_template, request, redirect

# Create the flask application object.
app = flask.Flask(__name__)

# Postnote site index.
@app.route('/', methods=['GET'])
def index():
    # Render the Postnote index template.
    return render_template('index')



if __name__ == '__main__':
    app.run(port = 8097, debug=True)

