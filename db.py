import datetime
import sqlite3



class DB:
    def __init__(self):
        self.db = sqlite3.connect("forms.db")
        self.cursor = self.db.cursor()


    def create_table_users(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                date DATE)
        """)
        self.db.commit()


    def add_user(self, username, first_name, last_name):
        self.cursor.execute("""
            INSERT INTO users (username, first_name, last_name, date)
            VALUES (?, ?, ?, ?)
        """,
    (username, first_name, last_name, datetime.datetime.now()))
        self.db.commit()


    def update_user(self, user_id, username=None, first_name=None, last_name=None):
        self.cursor.execute("""
            UPDATE users
            SET username =?, first_name =?, last_name =?
            WHERE id =?
        """, (username, first_name, last_name, user_id))
        self.db.commit()


    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id =?", (user_id,))
        self.db.commit()


    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()