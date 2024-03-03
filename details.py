import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def connect_db():
    connection = sqlite3.connect('hostelers.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        room_no INTEGER,
                        name TEXT,
                        contact_no TEXT,
                        address TEXT,
                        phone_no TEXT,
                        gender TEXT,
                        parents_name TEXT,
                        parents_phone_number  TEXT,
                        checkin_date TEXT,
                        checkout_date TEXT)''')
    connection.commit()
    return connection, cursor

def close_db(connection):
    connection.close()

def add_student():
    room_no = room_ent.get()
    name = name_ent.get()
    contact_no = contact_ent.get()
    address = address_ent.get()
    phone_no = phone_ent.get()
    gender = gender_combobox.get()
    parents_name = parents_ent.get()
    parents_number = phone_ent.get()

    checkin_date = entry_checkin.get()
    checkout_date = entry_checkout.get()
    
    if room_no and name and contact_no and address and phone_no and gender and parents_name and parents_number and checkin_date and checkout_date:
        if len(contact_no) != 10 or len(phone_no) != 10:
            messagebox.showerror("Error!", "Please enter a 10-digit contact number.", parent=win)
            return

        cursor.execute("INSERT INTO students (room_no, name, contact_no, address, phone_no, gender, parents_name, parents_phone_number, checkin_date, checkout_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(room_no, name, contact_no, address, phone_no, gender, parents_name, parents_number, checkin_date, checkout_date))
        connection.commit()
        view_students()
        clear_entries()
    else:
        messagebox.showerror("Error!", "Please fill in all the fields.", parent=win)

def view_students():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', 'end', values=row)

def search_students():
    search_value = search_entry.get()
    search_category = category_combobox.get()
    for row in tree.get_children():
        tree.delete(row)
    if search_category == "ID":
        cursor.execute("SELECT * FROM students WHERE id=?", (search_value,))
    elif search_category == "Room No":
        cursor.execute("SELECT * FROM students WHERE room_no=?", (search_value,))
    elif search_category == "Name":
        cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + search_value + '%',))
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', 'end', values=row)
    clear_entries()

def on_select(event):
    item = tree.selection()
    if item:
        edit_btn.grid(row=12, columnspan=2, pady=10)
        del_btn.grid(row=13, columnspan=2, pady=10)
        add_btn.grid_forget()
        
        selected_item = tree.item(item, 'values')
        room_ent.delete(0, tk.END)
        name_ent.delete(0, tk.END)
        contact_ent.delete(0, tk.END)
        address_ent.delete(0, tk.END)
        phone_ent.delete(0, tk.END)
        parents_ent.delete(0, tk.END)
        entry_checkin.delete(0, tk.END)
        entry_checkout.delete(0, tk.END)
        room_ent.insert(tk.END, selected_item[1])
        name_ent.insert(tk.END, selected_item[2])
        contact_ent.insert(tk.END, selected_item[3])
        address_ent.insert(tk.END, selected_item[4])
        phone_ent.insert(tk.END, selected_item[5])
        gender_combobox.set(selected_item[6])
        parents_ent.insert(tk.END, selected_item[7])
        entry_checkin.insert(tk.END, selected_item[8])
        entry_checkout.insert(tk.END, selected_item[9])
    else:
        add_btn.grid(row=11, columnspan=2, pady=10)
        edit_btn.grid_forget()
        del_btn.grid_forget()
        clear_entries()

def clear_entries():
    room_ent.delete(0, tk.END)
    name_ent.delete(0, tk.END)
    contact_ent.delete(0, tk.END)
    address_ent.delete(0, tk.END)
    phone_ent.delete(0, tk.END)
    parents_ent.delete(0, tk.END)
    gender_combobox.set('')
    entry_checkin.delete(0, tk.END)
    entry_checkout.delete(0, tk.END)

def edit_student():
    item = tree.selection()[0]
    selected_id = tree.item(item, 'values')[0]
    room_no = room_ent.get()
    name = name_ent.get()
    contact_no = contact_ent.get()
    address = address_ent.get()
    phone_no = phone_ent.get()
    gender = gender_combobox.get()
    parents_name = parents_ent.get()
    parents_number= phone_ent.get()
    checkin_date = entry_checkin.get()
    checkout_date = entry_checkout.get()
    cursor.execute("UPDATE students SET room_no=?, name=?, contact_no=?, address=?, phone_no=?, gender=?, parents_name=?, parents_phone_number=?, checkin_date=?, checkout_date=? WHERE id=?",(room_no, name, contact_no, address, phone_no, gender, parents_name, parents_number, checkin_date, checkout_date, selected_id))
    connection.commit()
    view_students()
    clear_entries()

def delete_student():
    item = tree.selection()[0]
    selected_id = tree.item(item, 'values')[0]
    cursor.execute("DELETE FROM students WHERE id=?", (selected_id,))
    connection.commit()
    view_students()
    clear_entries()

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Hostel Management System")

title_label = tk.Label(win, text="Hostel Management System", font=("Arial", 30, "bold"), border=12, relief=tk.GROOVE,
                       bg="lightblue")
title_label.pack(side=tk.TOP, fill=tk.X)

search_frame = tk.LabelFrame(win, text="Search", font=("Arial,20"), bd=12, relief=tk.GROOVE, bg="lightgrey")
search_frame.pack(side=tk.TOP, fill=tk.X)

placeholder_text = "Enter student ID or room no or student name"

search_entry = tk.Entry(search_frame, bd=7, font=("Arial", 10), fg='grey', width=60)
search_entry.insert(0, placeholder_text)
search_entry.bind('<FocusIn>', lambda event: search_entry.delete(0, tk.END) if search_entry.get() == placeholder_text else None)
search_entry.bind('<FocusOut>', lambda event: search_entry.insert(0, placeholder_text) if search_entry.get() == '' else None)
search_entry.grid(row=0, column=0, padx=10, pady=10)

category_combobox = ttk.Combobox(search_frame, values=["ID", "Room No", "Name"], state="readonly", font=("Arial", 10))
category_combobox.grid(row=0, column=2, padx=10, pady=10)
category_combobox.current(0)

search_btn = tk.Button(search_frame, text="Search", command=search_students)
search_btn.grid(row=0, column=3, padx=10, pady=5)

data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
data_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

detail_frame = tk.LabelFrame(data_frame, text="Enter Details", font=("Arial,20"), bd=12, relief=tk.GROOVE, bg="lightgrey")
detail_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

roomno_lbl = tk.Label(detail_frame, text="Room No", font=("Arial", 15), bg="lightgrey")
roomno_lbl.grid(row=0, column=0, padx=2,pady=2)

room_ent = tk.Entry(detail_frame, bd=0, font=("Arial", 15))
room_ent.grid(row=0, column=1, padx=2, pady=2)

name_lbl = tk.Label(detail_frame, text="Name", font=("Arial", 15), bg="lightgrey")
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name_ent = tk.Entry(detail_frame, bd=0, font=("Arial", 15))
name_ent.grid(row=1, column=1, padx=2, pady=2)

contact_lbl = tk.Label(detail_frame, text="Contact No", font=("Arial", 15), bg="lightgrey")
contact_lbl.grid(row=2, column=0, padx=2, pady=2)

contact_ent = tk.Entry(detail_frame, bd=0, font=("Arial", 15))
contact_ent.grid(row=2, column=1, padx=2, pady=2)

address_lbl = tk.Label(detail_frame, text="Address", font=("Arial", 15), bg="lightgrey")
address_lbl.grid(row=3, column=0, padx=2, pady=2)

address_ent = tk.Entry(detail_frame, bd=0, font=("Arial", 15))
address_ent.grid(row=3, column=1, padx=2, pady=2)

gender_lbl = tk.Label(detail_frame, text="Gender", font=("Arial", 15), bg="lightgrey")
gender_lbl.grid(row=4, column=0, padx=2, pady=2)

gender_combobox = ttk.Combobox(detail_frame, values=["Male", "Female","Others"], state="readonly", font=("Arial", 15))
gender_combobox.grid(row=4, column=1, padx=2, pady=2)

parents_lbl = tk.Label(detail_frame, text="Parent's Name", font=("Arial", 15), bg="lightgrey")
parents_lbl.grid(row=5, column=0, padx=2, pady=2)

parents_ent = tk.Entry(detail_frame, bd=0, font=("Arial", 15))
parents_ent.grid(row=5, column=1, padx=2, pady=2)

phone_lbl = tk.Label(detail_frame, text="Parent's Phone No", font=("Arial", 15), bg="lightgrey")
phone_lbl.grid(row=6, column=0, padx=2, pady=2)

phone_ent = tk.Entry(detail_frame, bd=0, font=("Arial", 15))
phone_ent.grid(row=6, column=1, padx=2, pady=2)

lbl_checkin_date = tk.Label(detail_frame, text="Check-In-Date", font=("Arial", 15), bg="lightgrey")
lbl_checkin_date.grid(row=7, column=0, padx=2, pady=2)

entry_checkin = ttk.Entry(detail_frame, font=("Arial", 15))
entry_checkin.grid(row=7, column=1, padx=2, pady=2)

lbl_checkout_date = tk.Label(detail_frame, text="Check-Out-Date", font=("Arial", 15), bg="lightgrey")
lbl_checkout_date.grid(row=8, column=0, padx=2, pady=2)

entry_checkout = ttk.Entry(detail_frame, font=("Arial", 15))
entry_checkout.grid(row=8, column=1, padx=2, pady=2)

add_btn = tk.Button(detail_frame, text="Add Student", command=add_student)
add_btn.grid(row=9, columnspan=2, pady=10)

edit_btn = tk.Button(detail_frame, text="Edit Student", command=edit_student)
edit_btn.grid(row=10, columnspan=2, pady=10)

del_btn = tk.Button(detail_frame, text="Delete Student", command=delete_student)
del_btn.grid(row=11, columnspan=2, pady=10)

tree_frame = tk.Frame(data_frame, bd=0, bg="lightgrey")
tree_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tree_scroll_y = tk.Scrollbar(tree_frame)
tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

tree_scroll_x = tk.Scrollbar(tree_frame, orient="horizontal")
tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

tree = ttk.Treeview(tree_frame, columns=('ID', 'Room No', 'Name', 'Contact No', 'Address', 'Phone No', 'Gender', "Parent's Name","Parent's Phone No", "Check-In-Date", "Check-Out-Date"), show='headings', yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
tree.heading('ID', text='Customer ID')
tree.heading('Room No', text='Room No')
tree.heading('Name', text='Name')
tree.heading('Contact No', text='Contact No')
tree.heading('Address', text='Address')
tree.heading('Phone No', text='Phone No')
tree.heading('Gender', text='Gender')
tree.heading("Parent's Name", text="Parent's Name")
tree.heading("Parent's Phone No", text="Parent's Phone No")
tree.heading("Check-In-Date", text="Check-In-Date")
tree.heading("Check-Out-Date", text="Check-Out-Date")
tree.pack(fill='both', expand=True)

tree_scroll_y.config(command=tree.yview)
tree_scroll_x.config(command=tree.xview)

tree.bind('<<TreeviewSelect>>', on_select)

connection, cursor = connect_db()

view_students()

win.mainloop()

close_db(connection)