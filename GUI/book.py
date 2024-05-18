from tkcalendar import Calendar
import customtkinter as ctk

class AddBook:
    def __init__(self, app_frame, back_action):
        self.formCard = ctk.CTkFrame(app_frame, width=600, height=500)

        self.title_label = ctk.CTkLabel(self.formCard, text="Add Book", font=ctk.CTkFont("Arial", size=42, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        self.title = ctk.CTkEntry(self.formCard, placeholder_text="Enter book title here", width=400)
        self.title.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

        self.ISBN = ctk.CTkEntry(self.formCard, placeholder_text="Enter ISBN here", width=400)
        self.ISBN.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

        self.desc_label = ctk.CTkLabel(self.formCard, text="description:", font=ctk.CTkFont("Arial", size=14, weight="bold"), text_color="grey")  
        self.desc_label.place(relx=0.25, rely=0.43, anchor=ctk.CENTER)  
        self.description = ctk.CTkTextbox(self.formCard, width=400, height=150)
        self.description.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        


        self.back_button = ctk.CTkButton(self.formCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.place(relx=0.01, rely=0.01, anchor=ctk.NW)


    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()



    
class UpdateBook:
    def __init__(self, app_frame, back_action):
        self.formCard = ctk.CTkFrame(app_frame, width=600, height=500)

        self.title_label = ctk.CTkLabel(self.formCard, text="Edit Book", font=ctk.CTkFont("Arial", size=42, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
        
        self.back_button = ctk.CTkButton(self.formCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.place(relx=0.01, rely=0.01, anchor=ctk.NW)


    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()