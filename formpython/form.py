from tkinter import *

import pyodbc

server = 'MONSTER\SQLEXPRESS'
bd = 'PassManager'
usr = 'userpython'
passwd = '123456789'


try:
    connectionServer = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+';DATABASE='+bd+';UID='+usr+';PWD='+passwd)
    print('connected')
except:
    print('Error connect')


def send_data():
    username_data = username.get()
    email_data = email.get()
    password_data = str(password.get())
    context_data = context.get()
    
    # print (username_data,email_data,password_data)

    cursor = connectionServer.cursor()
    cursor.execute("Select * from accountManager")

    query = "Insert into accountManager(Username,Email, Passwd, Context) values (?,?,?,?);"
    cursor.execute(query,username_data,email_data,password_data,context_data)
    cursor.commit()
    cursor.close()
    connectionServer.close()
    print("Succes")
    merge_label = Label(text="Succes", bg="#f9f9f9")
    merge_label.place(x=22,y=450)

   


window = Tk()
window.geometry("650x550")
window.title("Accounts Management")
window.resizable(False,False)
window.config(background = "#f9f9f9")
main_title = Label(text="Register form", font=("monospace", 13), bg="#f9f9f9",fg="#090909")
main_title.pack()

username_label = Label(text="Username", bg="#f9f9f9")
username_label.place(x=22, y=70)

email_label = Label(text="Email", bg="#f9f9f9")
email_label.place(x=22, y=130)

password_label = Label(text="Password", bg="#f9f9f9")
password_label.place(x=22, y=190)

context_label = Label(text="Context", bg="#f9f9f9")
context_label.place(x=22, y=250)


username = StringVar()
email = StringVar()
password = StringVar()
context = StringVar()

username_entry = Entry(textvariable=username, width="40")
email_entry = Entry(textvariable=email, width="40")
password_entry = Entry(textvariable=password, width="40", show="*")
context_entry = Entry(textvariable=context,width="40")

username_entry.place(x=22, y=100)
email_entry.place(x=22, y=160)
password_entry.place(x=22, y=220)
context_entry.place(x=22,y=280)

submit_btn = Button(window,text="Submit", command=send_data, width="30",height="2", bg="#f9f9f9")
submit_btn.place(x=22, y=360)

window.mainloop()

