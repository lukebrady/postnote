import hashlib

import mysql.connector as conn


class PostnoteDB:
    def __init__(self, host, user, passwd, database):
        self.db = conn.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )

    # Get the database connection object.
    def get_db_conn(self):
        print(self.db)
        return self.db

    # Create a new user. This will be called by the signup route.
    def create_new_user(self, username, email, password, user_type=1):
        # Create the cursor that will be used to create the user.
        cursor = self.db.cursor()
        # Check to see if the password has been filled in, if so hash the given password.
        if password != None:
            passhash = hashlib.sha256(password).hexdigest()
        else:
            return 1
        # Check to see if any of the fields do not match the database parameters.
        if len(username) > 50 or len(email) > 256:
            # Create the statement that will be used to create the new user.
            sql = 'INSERT INTO User (Username, Email, Password, UserType)' \
                  'VALUES ("{0}", "{1}", "{2}", "{3}")'.format(username, passhash, email, user_type)
            # Execute the query to create the user.
            try:
                cursor.execute(sql)
            except conn.Error:
                return 1
            cursor.close()
        else:
            return 1

    # Login a user and return session data.
    def login_user(self, username, password):
        # Create the cursor that will be used to query the database for the user.
        cursor = self.db.cursor()
        # Check to see if the password was provided.
        if password != None:
            passhash = hashlib.sha256(password).hexdigest()
        else:
            return 1
        # Now create the SQL statement that will retrieve the user information.
        sql = 'SELECT Username, Password FROM User WHERE Username = "{0}"'.format(username)
        # Try to query the database.
        try:
            cursor.execute(sql)
        except conn.Error:
            return 1
        result = cursor.fetchall()
        # Now compare the password hash with the supplied password's hash.
        if result[1] == passhash:
            return username
        else:
            return 1

    # Post a new note to the database.
    def post_note(self, title, message, username = 'lukebrains'):
        # Create a cursor to execute the post.
        cursor = self.db.cursor()
        # Prepare the SQL statement to insert the post into the database.
        sql = 'INSERT INTO Note (Title, Message, Username, NoteType)' \
              'VALUES ("{0}","{1}","{2}",0, CURDATE())'.format(title, message, username)
        # Now try and execute the query.
        try:
            cursor.execute(sql)
        except conn.Error:
            return 1
        # If the query was successful, return 0.
        cursor.close()
        return 0

    # Return a users notes from the database.
    def get_user_notes(self, username):
        # Create the cursor from the database object.
        cursor = self.db.cursor()
        # Create the SQL statement that will run against the Postnote database.
        sql = 'SELECT Title, Message FROM Notes WHERE Username = "{0}"'.format(username)
        # Now try to find the notes in the db.
        try:
            cursor.execute(sql)
        except conn.Error:
            return 1
        # If the query was successful, fetch all results.
        result = cursor.fetchall()
        # Close the connection then return the results.
        cursor.close()
        return result


if __name__ == '__main__':
    pndb = PostnoteDB(host='192.168.33.40', user='root', passwd='rootpassword1234', database='Postnote')
    pndb.get_db_conn()
