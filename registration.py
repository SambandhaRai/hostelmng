import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3

conn = sqlite3.connect('hostelers.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS User(
                UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName TEXT,
                lastName TEXT,
                gender   TEXT,
                streetAdd1 TEXT, 
                streetAdd2 TEXT,
                city       TEXT,
                phone   INT,
                email TEXT
                
    )''')
conn.commit()
conn.close()

def register():
    first_name_value = fnameEntry.get()
    last_name_value = lnameEntry.get()
    gender_value = var.get()
    address_value = staddress1Entry.get()
    address2_value =staddress2Entry.get()
    phone_value = phoneEntry.get()
    email_value = emailEntry.get()
    city_value = cityEntry.get()

    # Perform registration logic here
    print("Registration Details:")
    print("First Name:", first_name_value)
    print("Last Name:", last_name_value)
    print("Gender:", "Male" if gender_value == 1 else "Female")
    print("Address:", address_value)
    print("Phone Number:", phone_value)
    print("Email:", email_value)
    
    conn = sqlite3.connect('hostelers.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO User(firstName,lastName,gender,streetAdd1,streetAdd2,city,phone,email) VALUES (?,?,?,?,?,?,?,?)''',(first_name_value,last_name_value,gender_value,address_value,address2_value,city_value,phone_value,email_value))
    conn.commit()
    conn.close()

root = tk.Tk()
root.geometry('800x700')
root.title('Hostel Registration')

titleF = ttk.Frame(root)
titleL = ttk.Label(titleF, text='Hostel Registration Form', font=('Arial', 45), foreground='black')
titleF.pack()
titleL.pack(pady=20)

regis = tk.Frame(root, borderwidth=2, relief=tk.GROOVE)
regis.pack(fill=tk.X, padx=10, pady=10)

nameF = ttk.LabelFrame(regis, text='Full Name', labelanchor='n')
nameF.pack(expand=True, pady=10)

fname = ttk.Label(nameF, text='First Name:')
fname.grid(row=0, column=0, padx=5, pady=5, sticky='w')
fnameEntry = ttk.Entry(nameF)
fnameEntry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

lname = ttk.Label(nameF, text='Last Name:')
lname.grid(row=1, column=0, padx=5, pady=5, sticky='w')
lnameEntry = ttk.Entry(nameF)
lnameEntry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

othersF = ttk.LabelFrame(regis, text='Personal Info', labelanchor='n')
othersF.pack(expand=True, pady=10)

var = tk.IntVar()
gender_label = ttk.Label(othersF, text='Gender:')
gender_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

male = ttk.Radiobutton(othersF, text='Male', variable=var, value=1)
male.grid(row=1, column=0, padx=5, pady=5, sticky='w')

female = ttk.Radiobutton(othersF, text='Female', variable=var, value=2)
female.grid(row=1, column=1, padx=5, pady=5, sticky='w')

addressF = ttk.LabelFrame(regis, text='Address', labelanchor='n')
addressF.pack(expand=True, pady=10)

staddress1 = ttk.Label(addressF, text='Street Address:')
staddress1.grid(row=0, column=0, padx=5, pady=5, sticky='w')
staddress1Entry = ttk.Entry(addressF)
staddress1Entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

staddress2 = ttk.Label(addressF, text='Street Address Line 2:')
staddress2.grid(row=1, column=0, padx=5, pady=5, sticky='w')
staddress2Entry = ttk.Entry(addressF)
staddress2Entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

city = ttk.Label(addressF, text='City:')
city.grid(row=2, column=0, padx=5, pady=5, sticky='w')
cityEntry = ttk.Entry(addressF)
cityEntry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

state = ttk.Label(addressF, text='State/Province:')
state.grid(row=3, column=0, padx=5, pady=5, sticky='w')
stateEntry = ttk.Entry(addressF)
stateEntry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

contactF = ttk.LabelFrame(regis, text='Contacts', labelanchor='n')
contactF.pack(expand=True, pady=10)

phone = ttk.Label(contactF, text='Phone Number:')
phone.grid(row=0, column=0, padx=5, pady=5, sticky='w')
phoneEntry = ttk.Entry(contactF)
phoneEntry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

email = ttk.Label(contactF, text='Email:')
email.grid(row=1, column=0, padx=5, pady=5, sticky='w')
emailEntry = ttk.Entry(contactF)
emailEntry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

submit = ttk.Button(regis, text='Submit', command=register, style="TButton")
submit.pack(pady=20)

root.mainloop()