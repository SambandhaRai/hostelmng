import tkinter as tk
from tkinter import ttk
import sqlite3

class DormRoomStatusManagement(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dorm Room Status Management")
        self.geometry("1000x500")

        
        self.conn = sqlite3.connect('hostelers.db')
        self.create_database()  

        
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
        
        left_frame = tk.Frame(self, bg="lightgray", padx=20, pady=20)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)  

    
        right_frame = tk.Frame(self, bg="lightgray", padx=20, pady=20)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        
        for i, room in enumerate(self.rooms):
            self.create_room_widgets(left_frame, room)

        save_btn = tk.Button(left_frame, text="Save", command=self.save_data, bg="#4CAF50", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12))
        save_btn.pack(side=tk.BOTTOM, pady=(10,0))  


        
        columns = ("Room Number", "Vacancy", "Price Per Month", "Cleanliness")
        self.table = ttk.Treeview(right_frame, columns=columns, show="headings", selectmode="browse", height=15)
        for col in columns:
            self.table.heading(col, text=col)
        self.table.pack(fill=tk.BOTH, expand=True)
        self.update_table()

    def create_room_widgets(self, parent, room):
       
        dorm_frame = tk.Frame(parent, bg="lightgray", pady=10)
        dorm_frame.pack(fill=tk.X)

        tk.Label(dorm_frame, text=f"Room Number: {room['Room Number']}", bg="lightgray", font=("Arial", 12)).pack(side=tk.LEFT)
        vacancy_label = tk.Label(dorm_frame, text="Vacant" if room["Vacancy"] else "Occupied", fg="green" if room["Vacancy"] else "red", bg="lightgray", font=("Arial", 12))
        vacancy_label.pack(side=tk.LEFT, padx=(20,10))

        
        price_entry = tk.Entry(dorm_frame, textvariable=room["Price Per Month"], width=8, font=("Arial", 12))
        price_entry.pack(side=tk.LEFT)

  
        cleanliness_var = tk.StringVar(value=room["Cleanliness"].get()) 
        cleanliness_menu = ttk.OptionMenu(dorm_frame, cleanliness_var, room["Cleanliness"].get(), *["Clean", "Needs Cleaning", "Moderate"])
        cleanliness_menu.pack(side=tk.LEFT, padx=(20,0))
        cleanliness_menu.config(state="normal")
        room['cleanliness_var'] = cleanliness_var  

       
        book_button = tk.Button(dorm_frame, text="Book", command=lambda r=room: self.book_room(r, vacancy_label), bg="#2196F3", fg="white", bd=0, padx=5, pady=2, font=("Arial", 10))
        book_button.pack(side=tk.LEFT, padx=(20,0))

       
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
        
        for row in self.table.get_children():
            self.table.delete(row)
       
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

def main():
    app = DormRoomStatusManagement()
    app.mainloop()

if __name__ == "__main__":
    main()