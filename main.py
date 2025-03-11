import tkinter as tk

from db import DB


db = DB()  # создание базы данных
db.create_table_users()

def view_table(): # отображение таблицы
    users = db.get_all_users() # получение всех пользователей 
    list_box.delete(0, tk.END) # очистка всего текстового поля
    for user in users: # добавление информации про пользователей в поле
        list_box.insert(tk.END, f"{user[0]}: {user[1]} - {user[2]} {user[3]}")


def add_user(): 
    username = input_username.get() # получение итекста из полля ввода
    first_name = input_first_name.get()
    last_name = input_last_name.get()

    db.add_user(username, first_name, last_name) # добавление пользователя в базу данных
    view_table() # показ обновленной таблицы

def delete_user(): 
    selection = list_box.get(tk.ACTIVE) # получение выбранной строки из поля
    if selection: 
        user_id = int(selection.split(":")[0]) # получение id из этой строки 
        db.delete_user(user_id) # удаление пользователя из бд
        view_table() # показ обнолвенной таблицы

def update_user():
    selection = list_box.get(tk.ACTIVE)
    if selection:
        user_id = int(selection.split(":")[0])
        new_username = input_username.get()
        new_first_name = input_first_name.get()
        new_last_name = input_last_name.get()
        db.update_user(user_id, new_username, new_first_name, new_last_name)
        view_table()



root = tk.Tk() # создание корневого окна 
root.title("User Form") 


tk.Label(root, text="username").grid(row=0, column=0) # создание надписей и размещение их по сетке
tk.Label(root, text="имя").grid(row=1, column=0)
tk.Label(root, text="фамилия").grid(row=2, column=0)

input_username = tk.Entry(root) # создание полей ввода
input_first_name = tk.Entry(root)
input_last_name = tk.Entry(root)

input_username.grid(row=0, column=1) # размещение полей ввода по сетке
input_first_name.grid(row=1, column=1)
input_last_name.grid(row=2, column=1)

tk.Button(root, text="Добавить", command=add_user).grid(row=3, column=0) # создание и размещение кнопок по сетке
tk.Button(root, text="Изменить", command=update_user).grid(row=3, column=1)
tk.Button(root, text="Удалить", command=delete_user).grid(row=3, column=2)

list_box = tk.Listbox(root) # создание поля для отображение таблицы
list_box.grid(row=4, column=0, columnspan=3) # размещение этого поля по сетке


view_table() # показ всех пользователей 
root.mainloop() # запуск программы
