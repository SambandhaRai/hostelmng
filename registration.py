from tkinter import *
from tkinter import messagebox
import tkinter as ttk
import tkinter as tk
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title('Login')
root.geometry ('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

frame1=Frame(root,width=430,height=350).place(x=40,y=60)
logo=Image.open("/Users/sambandharai/Downloads/log123.png").resize((500,400))
logo_tk=ImageTk.PhotoImage(logo)
my_label=ttk.Label(frame1,image=logo_tk)
my_label.place(x=5,y=0)


conn = sqlite3.connect('hostelers.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS User(
                UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                password TEXT
    )''')
conn.commit()
conn.close()

def register():
    email_value = email.get()
    password_value = code.get()
    conpassword_value = code2.get()

    # Perform registration logic here
    print("Registration Details:")
    print("Email:", email_value)
    print("Password:",password_value,conpassword_value)
    
    conn = sqlite3.connect('hostelers.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO User(email,password) VALUES (?,?)''',(email_value,password_value))
    conn.commit()
    conn.close()

        


frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label (frame, text='Register',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light', 23, 'bold')) 
heading.place(x=100,y=5)


def on_enter(e) :
    email. delete(0, 'end')
def on_leave(e) :
    name=email.get()
    if name=='':
        email. insert(0, 'Email')

email = Entry(frame,width=25,fg='black',border=0, bg="white",font=( 'Microsoft YaHei UI Light',11))
email.place(x=30,y=80)
email.insert(0, 'Email')
email.bind('<FocusIn>', on_enter)
email.bind('<FocusOut>', on_leave)
Frame (frame, width=295, height=2,bg='black').place(x=25,y=107) 


def on_enter(e) :
    code.delete(0, 'end')
def on_leave(e) :
    name=code.get()
    if name=='':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0 ,bg="white", font=('Microsoft YaHei UI Light', 11))
code.place (x=30,y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame (frame,width=295,height=2,bg='black').place(x=25,y=177)


def on_enter(e) :
    code2.delete(0, 'end')
def on_leave(e) :
    name=code2.get()
    if name=='':
        code2.insert(0, 'Confirm Password')

code2 = Entry(frame, width=25, fg='black', border=0 ,bg="white", font=('Microsoft YaHei UI Light', 11))
code2.place (x=30,y=220)
code2.insert(0, 'Confirm Password')
code2.bind('<FocusIn>', on_enter)
code2.bind('<FocusOut>', on_leave)
Frame (frame, width=295, height=2,bg='black').place(x=25,y=247) 




Button (frame,width=39,pady=7,text='Confirm',bg='#57a1f8',fg='white' ,border=0, command=register).place(x=35,y=264)

def back():
    root.destroy()
    import log as log

bk = ttk.Button(frame,text="Back to Login",command=back)
bk.place(x=215,y=320)





root.mainloop()