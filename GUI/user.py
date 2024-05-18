import customtkinter as ctk

class Signup:

    def __init__(self, app_frame, back_action):
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

        self.signup_button = ctk.CTkButton(self.formCard, text="Signup", width=190)
        self.signup_button.place(relx=0.5, rely=0.92, anchor=ctk.CENTER)

        self.back_button = ctk.CTkButton(self.formCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.place(relx=0.01, rely=0.01, anchor=ctk.NW)

    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()




class UpdateUser:

    def __init__(self, app_frame, back_action):
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

        self.update_button = ctk.CTkButton(self.formCard, text="Update", width=190)
        self.update_button.place(relx=0.5, rely=0.92, anchor=ctk.CENTER)

        self.back_button = ctk.CTkButton(self.formCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.place(relx=0.01, rely=0.01, anchor=ctk.NW)

    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()
