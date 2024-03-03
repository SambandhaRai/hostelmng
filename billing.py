from tkinter import Tk, Label, Entry, Button, LabelFrame, IntVar, Text, Scrollbar, END, StringVar
import random
from datetime import datetime
from tkinter import messagebox
import sqlite3
import sys

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

        self.title_label = Label(self.win, text='Hostel Management System', font='Arial 25 bold', bg='#158aff', fg='white', bd=8, relief='groove')
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


def main():
    create_database()
    win = Tk()
    app = Loginpage(win)
    win.mainloop()


if __name__ == "__main__":
    main()
