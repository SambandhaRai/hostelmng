import tkinter as tk
import tkinter as ttk
from tkinter import Tk, Label, Entry, Button, LabelFrame, IntVar, Text, Scrollbar, END, StringVar
import random
from datetime import datetime
from tkinter import messagebox
import tkinter as ttk
import sqlite3
import sys
from PIL import ImageTk, Image

#============================================================================================Bill Page Import==========================================================================
def create_database():
    try:
        conn = sqlite3.connect('hostelers.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Hostel (
                id INTEGER PRIMARY KEY,
                customer_name TEXT,
                customer_contact TEXT,
                item_name TEXT,
                item_quantity INTEGER,
                cost_per_item REAL,
                bill_number INTEGER,
                date TEXT,
                total_cost REAL
            )
        ''')

        conn.commit()
        conn.close()
        print("Database created successfully!")
    except sqlite3.Error as e:
        print("Error creating database:", e)

class Loginpage:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1000x500")
        self.win.title("Hostel Management System")
        self.win.configure(bg='#f0f0f0') 

        self.title_label = Label(self.win, text='Hostel Accounts', font='Arial 25 bold', bg='#158aff', fg='white', bd=8, relief='groove')
        self.title_label.pack(side='top', fill='x')


        #######variables#########
        
        self.bill_no = random.randint(100, 9999)
        self.bill_no_tk = IntVar()
        self.bill_no_tk.set(self.bill_no)

        self.calc_var = StringVar()
        cust_nm = StringVar()
        cust_cot = StringVar()
        date_pr = StringVar()
        item_pur = StringVar()
        item_qty = StringVar()
        cone = StringVar()

        date_pr.set(datetime.now().date()) 
        total_list = []
        self.grd_total = 0

        #############entry#############

        self.entry_frame = LabelFrame(self.win, text='Enter Detail', bg='#f0f0f0', font=('Arial', 15), bd=7, relief='groove')
        self.entry_frame.place(x=20, y=60, width=450, height=430)

        self.bill_no_lbl = Label(self.entry_frame, text="Bill Number", font=('Arial', 12), bg='#f0f0f0')
        self.bill_no_lbl.grid(row=0, column=0, padx=2, pady=2)

        self.bill_no_ent = Entry(self.entry_frame, bd=5, font=('Arial', 12), textvariable=self.bill_no_tk)
        self.bill_no_ent.grid(row=0, column=1, padx=2, pady=2)
        self.bill_no_ent.config(state="disabled")

        self.cust_nm_lbl = Label(self.entry_frame, text="Customer Name", font=('Arial', 12), bg='#f0f0f0')
        self.cust_nm_lbl.grid(row=1, column=0, padx=2, pady=2)

        self.cust_nm_ent = Entry(self.entry_frame, bd=5, textvariable=cust_nm, font=('Arial', 12))
        self.cust_nm_ent.grid(row=1, column=1, padx=2, pady=2)

        self.cust_cot_lbl = Label(self.entry_frame, text="Customer Contact Number", font=('Arial', 12), bg='#f0f0f0')
        self.cust_cot_lbl.grid(row=2, column=0, padx=2, pady=2)

        self.cust_cot_ent = Entry(self.entry_frame, bd=5, textvariable=cust_cot, font=('Arial', 12))
        self.cust_cot_ent.grid(row=2, column=1, padx=2, pady=2)

        self.date_lbl = Label(self.entry_frame, text="Date", font=('Arial', 12), bg='#f0f0f0')
        self.date_lbl.grid(row=3, column=0, padx=2, pady=2)

        self.date_ent = Entry(self.entry_frame, bd=5, textvariable=date_pr, font=('Arial', 12))
        self.date_ent.grid(row=3, column=1, padx=2, pady=2)
        self.date_ent.config(state="disabled")

        self.Item_pur_lbl = Label(self.entry_frame, text="Item Name", font=('Arial', 12), bg='#f0f0f0')
        self.Item_pur_lbl.grid(row=4, column=0, padx=2, pady=2)

        self.Item_pur_ent = Entry(self.entry_frame, bd=5, textvariable=item_pur, font=('Arial', 12))
        self.Item_pur_ent.grid(row=4, column=1, padx=2, pady=2)

        self.Item_qty_lbl = Label(self.entry_frame, text="Item Quantity", font=('Arial', 12), bg='#f0f0f0')
        self.Item_qty_lbl.grid(row=5, column=0, padx=2, pady=2)

        self.Item_qty_ent = Entry(self.entry_frame, bd=5, textvariable=item_qty, font=('Arial', 12))
        self.Item_qty_ent.grid(row=5, column=1, padx=2, pady=2)

        self.cost_one_lbl = Label(self.entry_frame, text="Cost Per Item", font=('Arial', 12), bg='#f0f0f0')
        self.cost_one_lbl.grid(row=6, column=0, padx=2, pady=2)

        self.cost_one_ent = Entry(self.entry_frame, bd=5, textvariable=cone, font=('Arial', 12))
        self.cost_one_ent.grid(row=6, column=1, padx=2, pady=2)

        ###########function#########
        def default_bill():
            self.bill_txt.insert(END, "\t\t\t  Stay-In \n")
            self.bill_txt.insert(END, "\t\t\tcontact-977896765\n")
            self.bill_txt.insert(END, "=========================================================\n")
            self.bill_txt.insert(END, f"bill number:{self.bill_no_tk.get()}\n")

        def genbill():
            if cust_cot.get() == "" or (cust_cot.get() == "" or len(cust_cot.get()) != 10):
                messagebox.showerror("Error!", "please enter all the fields correctly.", parent=self.win)
            else:
                self.bill_txt.insert(END, f"\nCustomer Name : {cust_nm.get()}")
                self.bill_txt.insert(END, f"\nCustomer Contact : {cust_cot.get()}")
                self.bill_txt.insert(END, f"\nDate : {date_pr.get()}\n")
                self.bill_txt.insert(END, "=========================================================\n")
                self.bill_txt.insert(END, "product Name\t\t    Quantity\t\t    Per Cost\t\t    Total\n")
                self.bill_txt.insert(END,"=========================================================\n")
                self.add_btn.config(state="normal")
                self.total_btn.config(state="normal")

        def total_func():
            for item in total_list:
                self.grd_total = self.grd_total + item
            self.bill_txt.insert(END, "\n=========================================================\n")
            self.bill_txt.insert(END, f"\t\t\t\t Grand Total : {self.grd_total}   \n")
            self.bill_txt.insert(END, "=========================================================\n")
            self.save_btn.config(state="normal")

        def clear_func():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("")

        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state="normal")
            self.total_btn.config(state="normal")
            self.save_btn.config(state="normal")
            self.bill_txt.delete("1.0", END)
            default_bill()

        def add_func():
            if item_pur.get() == "" or item_qty.get() == "":
                messagebox.showerror("Error!", "please enter all the fields correctly.", parent=self.win)
            else:
                qty = int(item_qty.get())
                cones = int(cone.get())
                total = qty * cones
                total_list.append(total)
                self.bill_txt.insert(END, f"\n{item_pur.get()}\t\t    {item_qty.get()}\t\t    $ {cone.get()}\t\t   $ {total}  ")

        def save_func():
            user_choice = messagebox.askyesno("Conform?", f"Do you want to save the bill {self.bill_no_tk.get()}?", parent=self.win)
            if user_choice > 0:
                try:
                    conn = sqlite3.connect('hostelers.db')
                    cursor = conn.cursor()
                    cursor.execute('''
                        INSERT INTO Hostel (customer_name, customer_contact, item_name, item_quantity, cost_per_item, bill_number, date, total_cost)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (cust_nm.get(), cust_cot.get(), item_pur.get(), int(item_qty.get()), float(cone.get()), self.bill_no_tk.get(), date_pr.get(), self.grd_total))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", f"Bill {self.bill_no_tk.get()} has been saved successfully!", parent=self.win)
                except sqlite3.Error as e:
                    messagebox.showerror("Error", f"Error saving bill to database: {e}", parent=self.win)
            else:
                return

        ########botton#######

        self.botton_frame = LabelFrame(self.entry_frame, bd=5, text='option', bg='#f0f0f0', font=('Arial', 12))
        self.botton_frame.place(x=50, y=250, width=340, height=135)

        self.add_btn = Button(self.botton_frame, text='Add', font=('Arial', 12), width=10, height=2, command=add_func, bg='#158aff', fg='white')
        self.add_btn.grid(row=0, column=0, padx=4, pady=2)

        self.generate_btn = Button(self.botton_frame, text='Generate', font=('Arial', 12), width=10, height=2, command=genbill, bg='#158aff', fg='white')
        self.generate_btn.grid(row=0, column=1, padx=4, pady=2)

        self.clear_btn = Button(self.botton_frame, text='Clear', font=('Arial', 12), width=10, height=2, command=clear_func, bg='#158aff', fg='white')
        self.clear_btn.grid(row=0, column=2, padx=4, pady=2)

        self.total_btn = Button(self.botton_frame, text='Total', font=('Arial', 12), width=10, height=2, command=total_func, bg='#158aff', fg='white')
        self.total_btn.grid(row=1, column=0, padx=4, pady=2)

        self.reset_btn = Button(self.botton_frame, text='Reset', font=('Arial', 12), width=10, height=2, command=reset_func, bg='#158aff', fg='white')
        self.reset_btn.grid(row=1, column=1, padx=4, pady=2)

        self.save_btn = Button(self.botton_frame, text='Save', font=('Arial', 12), width=10, height=2, command=save_func, bg='#158aff', fg='white')
        self.save_btn.grid(row=1, column=2, padx=4, pady=2)

        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")

        ############bill##############

        self.bill_frame = LabelFrame(self.win, text="Bill Area", font=('Arial', 15), bg='#f0f0f0', bd=8, relief="groove")
        self.bill_frame.place(x=480, y=70, width=500, height=420)

        self.y_scroll = Scrollbar(self.bill_frame, orient="vertical")
        self.bill_txt = Text(self.bill_frame, bg="white", yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side='right', fill='y')
        self.bill_txt.pack(fill='both', expand=True)

        default_bill()
 #========================================================================================Bill PAge Import ENd===============================================================

#=========================================================================================STATUS PAGE IMPORT START===========================================================

import tkinter as tk
from tkinter import ttk
import sqlite3

class DormRoomStatusManagement(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dorm Room Status Management")
        self.geometry("1000x500")

        # Create SQLite database
        self.conn = sqlite3.connect('hostelers.db')
        self.create_database()  

        # Initialize dorm rooms
        self.rooms = [
            {"Room Number": "101", "Vacancy": True, "Price Per Month": tk.StringVar(value="500"), "Cleanliness": tk.StringVar(value="Clean")},
            {"Room Number": "102", "Vacancy": True, "Price Per Month": tk.StringVar(value="500"), "Cleanliness": tk.StringVar(value="Clean")},
            {"Room Number": "103", "Vacancy": True, "Price Per Month": tk.StringVar(value="500"), "Cleanliness": tk.StringVar(value="Clean")},
            {"Room Number": "104", "Vacancy": True, "Price Per Month": tk.StringVar(value="500"), "Cleanliness": tk.StringVar(value="Clean")},
            {"Room Number": "105", "Vacancy": True, "Price Per Month": tk.StringVar(value="500"), "Cleanliness": tk.StringVar(value="Clean")},
            {"Room Number": "106", "Vacancy": True, "Price Per Month": tk.StringVar(value="500"), "Cleanliness": tk.StringVar(value="Clean")},
        ]

        self.create_widgets()

    def create_database(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Room_Status (
                    room_number TEXT PRIMARY KEY,
                    vacancy TEXT,
                    price_per_month REAL,
                    cleanliness TEXT
                )
            ''')
            self.conn.commit()
            print("Database created successfully!")
        except sqlite3.Error as e:
            print("Error creating database:", e)

    def create_widgets(self):
        # Left frame to enclose widgets
        left_frame = tk.Frame(self, bg="lightgray", padx=20, pady=20)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)  

        # Right frame for displaying details in tabular form
        right_frame = tk.Frame(self, bg="lightgray", padx=20, pady=20)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create widgets for each dorm room
        for i, room in enumerate(self.rooms):
            self.create_room_widgets(left_frame, room)

        save_btn = tk.Button(left_frame, text="Save", command=self.save_data, bg="#4CAF50", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12))
        save_btn.pack(side=tk.BOTTOM, pady=(10,0))  


        # Display dorm room details in a table on the right frame
        columns = ("Room Number", "Vacancy", "Price Per Month", "Cleanliness")
        self.table = ttk.Treeview(right_frame, columns=columns, show="headings", selectmode="browse", height=15)
        for col in columns:
            self.table.heading(col, text=col)
        self.table.pack(fill=tk.BOTH, expand=True)
        self.update_table()

    def create_room_widgets(self, parent, room):
        # Dorm room details
        dorm_frame = tk.Frame(parent, bg="lightgray", pady=10)
        dorm_frame.pack(fill=tk.X)

        tk.Label(dorm_frame, text=f"Room Number: {room['Room Number']}", bg="lightgray", font=("Arial", 12)).pack(side=tk.LEFT)
        vacancy_label = tk.Label(dorm_frame, text="Vacant" if room["Vacancy"] else "Occupied", fg="green" if room["Vacancy"] else "red", bg="lightgray", font=("Arial", 12))
        vacancy_label.pack(side=tk.LEFT, padx=(20,10))

        # Price per month entry
        price_entry = tk.Entry(dorm_frame, textvariable=room["Price Per Month"], width=8, font=("Arial", 12))
        price_entry.pack(side=tk.LEFT)

        # Cleanliness status dropdown
        cleanliness_var = tk.StringVar(value=room["Cleanliness"].get()) 
        cleanliness_menu = ttk.OptionMenu(dorm_frame, cleanliness_var, room["Cleanliness"].get(), *["Clean", "Needs Cleaning", "Moderate"])
        cleanliness_menu.pack(side=tk.LEFT, padx=(20,0))
        cleanliness_menu.config(state="normal")
        room['cleanliness_var'] = cleanliness_var  

        # Book button for vacancy
        book_button = tk.Button(dorm_frame, text="Book", command=lambda r=room: self.book_room(r, vacancy_label), bg="#2196F3", fg="white", bd=0, padx=5, pady=2, font=("Arial", 10))
        book_button.pack(side=tk.LEFT, padx=(20,0))

        # Update button
        update_button = tk.Button(dorm_frame, text="Update", command=lambda r=room: self.update_room(r, vacancy_label, cleanliness_var, price_entry, update_button), bg="#FFA500", fg="white", bd=0, padx=5, pady=2, font=("Arial", 10))
        update_button.pack(side=tk.LEFT, padx=(20,0))

    def book_room(self, room, label):
        room["Vacancy"] = not room["Vacancy"]
        label.config(text="Vacant" if room["Vacancy"] else "Occupied", fg="green" if room["Vacancy"] else "red")
        self.update_table()
        self.update_database(room)

    def update_room(self, room, label, cleanliness_var, price_entry, update_button):
        room["Cleanliness"].set(cleanliness_var.get())
        room["Price Per Month"].set(price_entry.get())
        self.update_table()
        self.update_database(room)
        update_button.config(state="normal")  
        
    def update_database(self, room):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE Room_Status
                SET vacancy = ?,
                    price_per_month = ?,
                    cleanliness = ?
                WHERE room_number = ?
            ''', ("Vacant" if room["Vacancy"] else "Occupied", float(room["Price Per Month"].get()), room['cleanliness_var'].get(), room["Room Number"]))
            self.conn.commit()
            print("Database updated successfully!")
        except sqlite3.Error as e:
            print("Error updating database:", e)

    def update_table(self):
        # Clear previous data
        for row in self.table.get_children():
            self.table.delete(row)
        # Populate table with updated data
        for room in self.rooms:
            self.table.insert("", "end", values=(room["Room Number"], "Vacant" if room["Vacancy"] else "Occupied", room["Price Per Month"].get(), room["Cleanliness"].get()))

    def save_data(self):
        for room in self.rooms:
            self.save_to_database(room)


    def save_to_database(self, room):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO Room_Status (room_number, vacancy, price_per_month, cleanliness)
                VALUES (?, ?, ?, ?)
            ''', (room["Room Number"], "Vacant" if room["Vacancy"] else "Occupied", float(room["Price Per Month"].get()), room["Cleanliness"].get()))
            self.conn.commit()
            print("Room added to the database successfully!")
        except sqlite3.Error as e:
            print("Error adding room to the database:", e)


#=======================================================================================STATUS PAGE IMPORT eND=============================================================
            
#=======================================================================================Details Import Start===============================================================
def open_book_page():

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

            
#=======================================================================================Detailss PAge Import End===========================================================
            
class StayInHostelHomePage(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title("Stay-In Hostel Management")
        self.geometry("950x500")
        self.configure(background="#f0f0f0")

        logo=Image.open("C:/Users/Acer/Desktop/REAL PROJECT WORKS COMMIT/log123.png").resize((500,400))
        logo_tk=ImageTk.PhotoImage(logo)
        my_label=ttk.Label(self,image=logo_tk)
        my_label.place(x=5,y=0)

        self.create_header()
        self.create_main_content()
        self.create_footer()

    def create_header(self):

        header_frame = tk.Frame(self, bg="#158aff", height=60)  
        header_frame.pack(fill=tk.X)

        header_label = tk.Label(header_frame, text="Stay-In Hostel Management", font=("Arial", 24), fg="white", bg="#158aff")
        header_label.pack(padx=20, pady=10)



    def create_main_content(self):

        def open_bill_page():
            self.destroy()
            win = Tk()
            app = Loginpage(win)
            win.mainloop()

        def open_room_status():
            dorm_management = DormRoomStatusManagement()
            dorm_management.mainloop()

        main_frame = tk.Frame(self, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

        # Room Status Frame
        room_status_frame = tk.LabelFrame(main_frame, text="Room Status", font=("Arial", 18), bg="#f0f0f0", padx=20, pady=10, width=350, height=400)  
        room_status_frame.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        check_room_status_button = tk.Button(room_status_frame, text="Check Room Status", font=("Arial", 12), bg="#158aff", fg="white", padx=10, pady=5, bd=0, command=open_room_status)
        check_room_status_button.pack(padx=20, pady=10)

        # Room Details Frame
        room_details_frame = tk.LabelFrame(main_frame, text="Room Details", font=("Arial", 18), bg="#f0f0f0", padx=20, pady=10, width=350, height=400,) 
        room_details_frame.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        view_room_details_button = tk.Button(room_details_frame, text="View Room Details", font=("Arial", 12), bg="#158aff", fg="white", padx=10, pady=5, bd=0,command=open_book_page )
        view_room_details_button.pack(padx=20, pady=10)

        
        # Accounts Frame
        accounts_frame = tk.LabelFrame(main_frame, text="Accounts", font=("Arial", 18), bg="#f0f0f0", padx=20, pady=10, width=500, height=900) 
        accounts_frame.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        manage_accounts_button = tk.Button(accounts_frame, text="Manage Accounts", font=("Arial", 12), bg="#158aff", fg="white", padx=10, pady=5, bd=0,command=open_bill_page)
        manage_accounts_button.pack(padx=20, pady=10)

    def create_footer(self):

        footer_label = tk.Label(self, text="© 2024 Stay-In Hostel Management. All rights reserved.", font=("Arial", 10), fg="gray", bg="#f0f0f0")
        footer_label.pack(side=tk.BOTTOM, fill=tk.X)



if __name__ == "__main__":

    app = StayInHostelHomePage()
    app.mainloop()
