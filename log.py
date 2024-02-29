from tkinter import *
from tkinter import messagebox
import tkinter as ttk
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



#log function
def login():
    em = email.get()
    password = code.get()

    conn = sqlite3.connect("hostelers.db")
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE email=? AND password=?",(em,password))
    authenticated_email = c.fetchone()

    if authenticated_email:
        root.destroy()
        import registration as registration
    elif em == "" or password == "":
        messagebox.showerror("Invalid","Please fill out the fields")
    else:
        messagebox.showerror("Invalid","Invalid Email and Password")


        


frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label (frame, text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light', 23, 'bold')) 
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

Button (frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white' ,border=0, command=login).place(x=35,y=204)
label=Label(frame, text="Don't have an account?", fg='black',bg='white', font=( 'Microsoft YaHei UI Light' ,9))
label. place (x=75,y=270)

def sign():
    root.destroy()#destroys the login window
    import registration as registration#imports code of registration
#RegisterWay
sign_up= Button(frame,width=6, text='Sign up' ,border=0,bg='white', cursor='hand2',fg='#57a1f8',command=sign)
sign_up.place(x=215, y=270)



root.mainloop()