import tkinter as tk
import mysql.connector
from tkinter import *


def submitact():

    user = Username.get()
    passw = password.get()
    if user or passw == "":
        print('voce tem que dgitar uma senha ou o usuario')

    print(f"voce digitou {user} {passw}")

    logintodb(user, passw)


def logintodb(user, passw):

    if passw:
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="marcos",
                                     db="python")
        cursor = db.cursor()

    savequery = f"select * from cadastro where nome='{user}' and senha='{passw}';"

    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()

        for x in myresult:
            if x != "":
                print(x)
                print("Query Excecuted successfully")
            else:
                print(x)
                print("senha ou login inesistente")
    except:
        db.rollback()
        print("Error occured")


root = tk.Tk()
root.geometry("300x200")
root.title("Tela de Login")


lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=50, y=50)

password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)

submitbtn = tk.Button(root, text="Login",
                      bg='blue', command=submitact)
submitbtn.place(x=150, y=135, width=55)

root.mainloop()
