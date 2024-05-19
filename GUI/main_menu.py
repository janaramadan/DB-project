import customtkinter as ctk

class MainMenu:
    def __init__(self, app_frame, signup, update_user, add_book, update_book, view_books):
        self.menu = ctk.CTkFrame(app_frame, width=600, height=500)

        self.title_label = ctk.CTkLabel(self.menu, text="Main Menu", font=ctk.CTkFont("Arial", size=42, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)    

        self.signup = ctk.CTkButton(self.menu, text="Signup", command=signup)
        self.signup.place(relx=0.3, rely=0.4, anchor=ctk.CENTER)

        self.update_user = ctk.CTkButton(self.menu, text="Edit User Data", command=update_user)
        self.update_user.place(relx=0.7, rely=0.4, anchor=ctk.CENTER)

        self.add_book = ctk.CTkButton(self.menu, text="Add Book", command=add_book)
        self.add_book.place(relx=0.3, rely=0.6, anchor=ctk.CENTER)

        self.update_book = ctk.CTkButton(self.menu, text="Update Book", command=update_book)
        self.update_book.place(relx=0.7, rely=0.6, anchor=ctk.CENTER)

        self.view_books = ctk.CTkButton(self.menu, text="View Books", command=view_books)
        self.view_books.place(relx=0.3, rely=0.8, anchor=ctk.CENTER)
        
        self.search_books = ctk.CTkButton(self.menu, text="search Books")
        self.search_books.place(relx=0.7, rely=0.8, anchor=ctk.CENTER)
    
    def show(self):
        self.menu.pack(pady=(50, 0))

    def hide(self):
        self.menu.pack_forget()