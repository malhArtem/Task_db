import sqlite3


connect = sqlite3.connect("database.db")

cursor = connect.cursor()

def create_tables():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    lastname TEXT,
                    age INTEGER
                    )""")
    connect.commit()


def add_user(name, lastname, age):
    cursor.execute("INSERT INTO users(name=?, lastname=?, age=?)", (name, lastname, age))
    connect.commit()


def get_all():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return users


def get_users_by_id(id: int):
    cursor.execute("SELECT * FROM users WHERE id=?", (id,))
    user = cursor.fetchone()
    return user


def update_user():
    pass


def delete_user():
    pass





connect.commit()
cursor.execute("SELECT * FROM users WHERE name=?", 
                (name,))


