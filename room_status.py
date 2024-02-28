import tkinter as tk
from tkinter import ttk

class DormRoomStatusManagement(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dorm Room Status Management")
        self.geometry("1000x500")

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

    def create_widgets(self):
        # Left frame to enclose widgets
        left_frame = tk.Frame(self, bg="lightgray", padx=20, pady=20)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)  # Expanded vertically

        # Right frame for displaying details in tabular form
        right_frame = tk.Frame(self, bg="lightgray", padx=20, pady=20)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create widgets for each dorm room
        for i, room in enumerate(self.rooms):
            self.create_room_widgets(left_frame, room)

        # Button to manually add a room
        add_room_btn = tk.Button(left_frame, text="Add Room", command=self.add_room_dialog, bg="#4CAF50", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12))
        add_room_btn.pack(side=tk.BOTTOM, pady=(20,0))  # Placed at the bottom

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
        cleanliness_menu = ttk.OptionMenu(dorm_frame, room["Cleanliness"], room["Cleanliness"].get(), *["Clean", "Needs Cleaning", "Moderate"])
        cleanliness_menu.pack(side=tk.LEFT, padx=(20,0))

        # Toggle button for vacancy
        toggle_button = tk.Button(dorm_frame, text="Toggle", command=lambda r=room: self.toggle_vacancy(r, vacancy_label), bg="#2196F3", fg="white", bd=0, padx=5, pady=2, font=("Arial", 10))
        toggle_button.pack(side=tk.LEFT, padx=(20,0))

    def toggle_vacancy(self, room, label):
        room["Vacancy"] = not room["Vacancy"]
        label.config(text="Vacant" if room["Vacancy"] else "Occupied", fg="green" if room["Vacancy"] else "red")
        self.update_table()

    def update_table(self):
        # Clear previous data
        for row in self.table.get_children():
            self.table.delete(row)
        # Populate table with updated data
        for room in self.rooms:
            self.table.insert("", "end", values=(room["Room Number"], "Vacant" if room["Vacancy"] else "Occupied", room["Price Per Month"].get(), room["Cleanliness"].get()))

    def add_room_dialog(self):
        dialog = AddRoomDialog(self)
        self.wait_window(dialog)

class AddRoomDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Add Room")
        self.geometry("300x300")

        self.room_number = tk.StringVar()
        self.vacancy = tk.BooleanVar()
        self.price_per_month = tk.StringVar()
        self.cleanliness = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Room Number:", font=("Arial", 12)).pack(pady=(10,0))
        tk.Entry(self, textvariable=self.room_number, font=("Arial", 12)).pack()

        tk.Checkbutton(self, text="Vacant", variable=self.vacancy, font=("Arial", 12)).pack()

        tk.Label(self, text="Price Per Month:", font=("Arial", 12)).pack(pady=(10,0))
        tk.Entry(self, textvariable=self.price_per_month, font=("Arial", 12)).pack()

        tk.Label(self, text="Cleanliness:", font=("Arial", 12)).pack(pady=(10,0))
        ttk.OptionMenu(self, self.cleanliness, "Clean", "Needs Cleaning", "Moderate").pack()

        add_btn = tk.Button(self, text="Add", command=self.add_room, bg="#4CAF50", fg="white", bd=0, padx=10, pady=5, font=("Arial", 12))
        add_btn.pack(pady=10)

    def add_room(self):
        new_room = {
            "Room Number": self.room_number.get(),
            "Vacancy": self.vacancy.get(),
            "Price Per Month": tk.StringVar(value=self.price_per_month.get()),
            "Cleanliness": tk.StringVar(value=self.cleanliness.get())
        }
        self.parent.rooms.append(new_room)
        self.parent.create_room_widgets(self.parent.winfo_children()[0], new_room)
        self.parent.update_table()
        self.destroy()

def main():
    app = DormRoomStatusManagement()
    app.mainloop()

if __name__ == "__main__":
    main()
