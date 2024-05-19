import customtkinter as ctk

def insertStudent(cursor, password, username, email, country, city, street):
    cursor.execute(
        "INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES (?, ?, ?, ?, ?, ?)",
        (password, username, email, country, city, street)
    )

def insertAdmin(cursor, password, username, email, country, city, street):
    cursor.execute(
        "INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES (?, ?, ?, ?, ?, ?)",
        (password, username, email, country, city, street)
    )

def getStudents(cursor):
    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()
    print("Students:")
    for student in students:
        print(student)

def getAdmins(cursor):
    cursor.execute("SELECT * FROM Admin")
    admins = cursor.fetchall()
    print("Admins:")
    for admin in admins:
        print(admin)

class Signup:

    def __init__(self, app_frame, cursor, back_action):
        self.cursor = cursor
        self.formCard = ctk.CTkFrame(app_frame, width=600, height=500)

        self.title_label = ctk.CTkLabel(self.formCard, text="Signup", font=ctk.CTkFont("Arial", size=42, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        self.username = ctk.CTkEntry(self.formCard, placeholder_text="Enter username here", width=400)
        self.username.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

        self.email = ctk.CTkEntry(self.formCard, placeholder_text="Enter email here", width=400)
        self.email.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

        self.street = ctk.CTkEntry(self.formCard, placeholder_text="Enter your street", width=400)
        self.street.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

        self.city = ctk.CTkEntry(self.formCard, placeholder_text="Enter your city", width=400)
        self.city.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)

        self.country = ctk.CTkEntry(self.formCard, placeholder_text="Enter your country", width=400)
        self.country.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)

        self.password = ctk.CTkEntry(self.formCard, placeholder_text="Enter password here", show="*", width=400)
        self.password.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)

        self.is_admin = ctk.CTkCheckBox(self.formCard , text="Is this admin account?",checkbox_height=18, checkbox_width=18)
        self.is_admin.place(relx=0.5, rely=0.84, anchor=ctk.CENTER)

        self.signup_button = ctk.CTkButton(self.formCard, text="Signup", width=190, command=self.signup_action)
        self.signup_button.place(relx=0.5, rely=0.92, anchor=ctk.CENTER)

        self.back_button = ctk.CTkButton(self.formCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.place(relx=0.01, rely=0.01, anchor=ctk.NW)

    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()

    def reset(self):
        self.username.delete(0, ctk.END)
        self.email.delete(0, ctk.END)
        self.street.delete(0, ctk.END)
        self.city.delete(0, ctk.END)
        self.country.delete(0, ctk.END)
        self.password.delete(0, ctk.END)
        self.is_admin.deselect()
    
    def signup_action(self):
        if self.is_admin.get():
            insertAdmin(self.cursor, self.password.get(), self.username.get(), self.email.get(), self.country.get(), self.city.get(),self.street.get())
            getAdmins(self.cursor)
        else:
            insertStudent(self.cursor, self.password.get(), self.username.get(), self.email.get(), self.country.get(), self.city.get(),self.street.get())
            getStudents(self.cursor)
        self.cursor.commit()
        self.reset()




class UpdateUser:

    def __init__(self, app_frame, cursor, back_action):
        self.formCard = ctk.CTkFrame(app_frame, width=600, height=500)

        self.title_label = ctk.CTkLabel(self.formCard, text="Update User", font=ctk.CTkFont("Arial", size=42, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        self.username = ctk.CTkEntry(self.formCard, placeholder_text="Enter username here", width=400)
        self.username.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

        self.email = ctk.CTkEntry(self.formCard, placeholder_text="Enter email here", width=400)
        self.email.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

        self.street = ctk.CTkEntry(self.formCard, placeholder_text="Enter your street", width=400)
        self.street.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

        self.city = ctk.CTkEntry(self.formCard, placeholder_text="Enter your city", width=400)
        self.city.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)

        self.country = ctk.CTkEntry(self.formCard, placeholder_text="Enter your country", width=400)
        self.country.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)

        self.password = ctk.CTkEntry(self.formCard, placeholder_text="Enter password here", show="*", width=400)
        self.password.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)

        self.is_admin = ctk.CTkCheckBox(self.formCard , text="Is this admin account?",checkbox_height=18, checkbox_width=18)
        self.is_admin.place(relx=0.5, rely=0.84, anchor=ctk.CENTER)

        self.update_button = ctk.CTkButton(self.formCard, text="Update", width=190, command=self.update_action)
        self.update_button.place(relx=0.5, rely=0.92, anchor=ctk.CENTER)

        self.back_button = ctk.CTkButton(self.formCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.place(relx=0.01, rely=0.01, anchor=ctk.NW)

    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()
    
    def reset(self):
        self.username.delete(0, ctk.END)
        self.email.delete(0, ctk.END)
        self.street.delete(0, ctk.END)
        self.city.delete(0, ctk.END)
        self.country.delete(0, ctk.END)
        self.password.delete(0, ctk.END)
        self.is_admin.deselect()

    def update_action(self):
        # self.cursor.commit()
        self.reset()
        pass