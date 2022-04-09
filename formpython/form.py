import tkinter as tk
from tkinter import ttk, font
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

    cursor = connectionServer.cursor()
    cursor.execute("Select * from accountManager")

    query = "Insert into accountManager(Username,Email, Passwd, Context) values (?,?,?,?);"
    cursor.execute(query,username_data,email_data,password_data,context_data)
    cursor.commit()
    cursor.close()
    connectionServer.close()
    print("Succes")
    merge_label = tk.Label(text="Succes", background="#f9f9f9",font=font.Font(size=16))
    merge_label.place(x=22,y=450)

#var global   
spaceElement = 100

window = tk.Tk()
window.geometry("650x550")
window.title("Accounts Management")
window.resizable(False,False)
window.config(background = "#f9f9f9")
main_title = tk.Label(text="Accounts Management", font=font.Font(size=18), bg="#f9f9f9",fg="#090909")
main_title.pack()

username_label = tk.Label(text="Username", bg="#f9f9f9",font=font.Font(size=14))
username_label.place(x=22, y=80-3)


email_label = tk.Label(text="Email", bg="#f9f9f9",font=font.Font(size=14))
email_label.place(x=22, y=spaceElement+80-3)

password_label = tk.Label(text="Password", bg="#f9f9f9",font=font.Font(size=14))
password_label.place(x=22, y=spaceElement+180-3)

context_label = tk.Label(text="Context", bg="#f9f9f9",font=font.Font(size=14))
context_label.place(x=22, y=spaceElement+280-3)

#Styles
style = ttk.Style()
style.configure(
        "MyEntry.TEntry",
        padding=10,
        font=font.Font(family="monospace",size=13)
        ) 

username = tk.StringVar()
email = tk.StringVar()
password = tk.StringVar() 
context = tk.StringVar()

username_entry = ttk.Entry(textvariable=username,style="MyEntry.TEntry",width=40)
email_entry = ttk.Entry(textvariable=email,style="MyEntry.TEntry",width=40)
password_entry = ttk.Entry(textvariable=password,style="MyEntry.TEntry" , show="*",width=40)
context_entry = ttk.Entry(textvariable=context,style="MyEntry.TEntry",width=40)

username_entry.place(x=22, y=100)
email_entry.place(x=22, y=spaceElement*2)
password_entry.place(x=22, y=spaceElement*3)
context_entry.place(x=22,y=spaceElement*4)

submit_btn = tk.Button(window,text="Submit",font=font.Font(size=12),fg="#f09800", command=send_data, width="24",height="2", bg="#f0f880", border=0)
submit_btn.place(x=40, y=500)

window.mainloop()

