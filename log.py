from tkinter import *
from tkinter import messagebox
import tkinter as ttk
from PIL import ImageTk,Image

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

def signin():
    username = user.get()
    password = code.get()

    if username == 'user' and password == 'user123':
       
       screen=Toplevel(root)
       screen. title("App")
       screen.geometry ('925x500+300+200')
       screen.config(bg="white") 

       Label(screen, text='Hello Everyone!',bg='#fff', font=( 'Calibri(Body)', 50, 'bold')).pack(expand= True) 

       screen.mainloop()

    elif username!= 'user' and password!= 'user123':
        messagebox.showerror("Invalid", "invalid username and password")
    
    elif password!= "user123":
         messagebox.showerror("Invalid", "invalid password")
    
    elif username!= "user":
         messagebox.showerror("Invalid", "invalid password")
       
   


frame=Frame(root,width=350,height=350,bg="white")
frame. place(x=480,y=70)

heading=Label (frame, text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light', 23, 'bold')) 
heading.place(x=100,y=5)


def on_enter(e) :
    user. delete(0, 'end')
def on_leave(e) :
    name=user.get()
    if name=='':
        user. insert(0, 'Username')

user = Entry(frame,width=25,fg='black',border=0, bg="white",font=( 'Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
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

Button (frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white' ,border=0, command= signin).place(x=35,y=204)
label=Label(frame, text="Don't have an account?", fg='black',bg='white', font=( 'Microsoft YaHei UI Light' ,9))
label. place (x=75,y=270)

def sign():
    root.destroy()#destroys the login window
    import ok.registration as registration#imports code of registration
#RegisterWay
sign_up= Button(frame,width=6, text='Sign up' ,border=0,bg='white', cursor='hand2',fg='#57a1f8',command=sign)
sign_up.place(x=215, y=270)




root.mainloop()