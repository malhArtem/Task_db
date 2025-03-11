import tkinter as tk

from db import DB


db = DB()
db.create_table_users()

def view_table():
    users = db.get_all_users()
    list_box.delete(0, tk.END)
    for user in users:
        list_box.insert(tk.END, f"{user[0]}: {user[1]} - {user[2]} {user[3]}")


def add_user():
    username = input_username.get()
    first_name = input_first_name.get()
    last_name = input_last_name.get()

    db.add_user(username, first_name, last_name)
    view_table()

def delete_user():
    selection = list_box.get(tk.ACTIVE)
    if selection:
        user_id = int(selection.split(":")[0])
        db.delete_user(user_id)
        view_table()

def update_user():
    selection = list_box.get(tk.ACTIVE)
    if selection:
        user_id = int(selection.split(":")[0])
        new_username = input_username.get()
        new_first_name = input_first_name.get()
        new_last_name = input_last_name.get()
        db.update_user(user_id, new_username, new_first_name, new_last_name)
        view_table()



root = tk.Tk()
root.title("User Form")


tk.Label(root, text="username").grid(row=0, column=0)
tk.Label(root, text="имя").grid(row=1, column=0)
tk.Label(root, text="фамилия").grid(row=2, column=0)

input_username = tk.Entry(root)
input_first_name = tk.Entry(root)
input_last_name = tk.Entry(root)

input_username.grid(row=0, column=1)
input_first_name.grid(row=1, column=1)
input_last_name.grid(row=2, column=1)

tk.Button(root, text="Добавить", command=add_user).grid(row=3, column=0)
tk.Button(root, text="Изменить", command=update_user).grid(row=3, column=1)
tk.Button(root, text="Удалить", command=delete_user).grid(row=3, column=2)

list_box = tk.Listbox(root)
list_box.grid(row=4, column=0, columnspan=3)


view_table()
root.mainloop()
