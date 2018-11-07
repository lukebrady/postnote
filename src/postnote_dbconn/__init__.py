import mysql.connector as conn

class PostnoteDB:
    def __init__(self):
        self.db = conn.connect(
            host='192.168.33.40',
            user='root',
            passwd='rootpassword1234',
            database='Postnote'
        )
    def get_db_conn(self):
        print(self.db)



if __name__ == '__main__':
    pndb = PostnoteDB()
    pndb.get_db_conn()