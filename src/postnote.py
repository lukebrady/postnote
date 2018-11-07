import flask, json
from flask import render_template, redirect, session, request
from flask_cors import cross_origin
from pndb import PostnoteDB

# Create the flask application object.
app = flask.Flask(__name__)
# These settings should be changed when hosting your own instance of Postnote.
# Also, this is a local database and similar settings should not be used in production.
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
@app.route('/post/<user>', methods=['GET', 'POST'])
@cross_origin()
def post(user):
    if request.method == 'POST':
        # Get the JSON from the request.
        req_json = request.json
        print(req_json)
        # Check to see if the request included a title and message.
        if req_json['Title'] and req_json['Message']:
            result = conn.post_note(req_json['Title'], req_json['Message'])
            if result != 1:
                return 'Successfully posted {}.'.format(req_json['Title'])
            else:
                return 'There was an issue posting {}.'.format(req_json['Title'])

    if 'username' in session:
        return render_template('welcome')
    return redirect('/')

@app.route('/notes/<user>', methods=['GET'])
@cross_origin()
def get_notes(user):
    result = []
    # Retrieve the user's notes. This route serves public notes.
    notes = conn.get_user_notes(user)
    if notes != 1:
        # Build a JSON array and return.
        for note in notes:
            result.append({notes[0], notes[1]})
        json_result = json.dumps(result)
        return json_result
    else:
        return 'Could not retrieve note data for {}.'.format(user)

if __name__ == '__main__':
    app.run(port=8097, debug=True)
