import customtkinter as ctk

def insertBook(cursor, isbn, publish_year, description, pages, title):
    cursor.execute(
        "INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (?, ?, ?, ?, ?)",
        (isbn, publish_year, description, pages, title)
    )

class AddBook:
    def __init__(self, app_frame, cursor, back_action):
        self.cursor = cursor
        self.formCard = ctk.CTkFrame(app_frame, width=600, height=500)

        self.title_label = ctk.CTkLabel(self.formCard, text="Add Book", font=ctk.CTkFont("Arial", size=42, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        self.title = ctk.CTkEntry(self.formCard, placeholder_text="Enter book title here", width=400)
        self.title.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.ISBN = ctk.CTkEntry(self.formCard, placeholder_text="Enter ISBN here", width=400)
        self.ISBN.place(relx=0.5, rely=0.28, anchor=ctk.CENTER) 

        self.desc_label = ctk.CTkLabel(self.formCard, text="Description:", font=ctk.CTkFont("Arial", size=14, weight="bold"), text_color="grey")  
        self.desc_label.place(relx=0.24, rely=0.35, anchor=ctk.CENTER)  
        self.description = ctk.CTkTextbox(self.formCard, width=400, height=120, fg_color="#343638", border_color="#565b5e",border_width=2)
        self.description.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        self.cat_label = ctk.CTkLabel(self.formCard, text="Category:", font=ctk.CTkFont("Arial", size=14, weight="bold"), text_color="grey")  
        self.cat_label.place(relx=0.24, rely=0.67, anchor=ctk.CENTER)  
        options = ["Any", "Science", "Adventure", "Philosophy", "Mystery", "History", "Drama", "Romance", "Fantasy"]
        self.category = ctk.CTkComboBox(self.formCard, values=options)
        self.category.place(relx=0.44, rely=0.67, anchor=ctk.CENTER)

        self.pub_date = ctk.CTkEntry(self.formCard, placeholder_text="Enter publication date (YYYY-MM-DD)", width=400)
        self.pub_date.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)  

        self.pages_num = ctk.CTkEntry(self.formCard, placeholder_text="Enter the number of pages", width=400)
        self.pages_num.place(relx=0.5, rely=0.83, anchor=ctk.CENTER)  
        
        self.add_button = ctk.CTkButton(self.formCard, text="Add", command=self.add_action)
        self.add_button.place(relx=0.5, rely=0.92, anchor=ctk.CENTER)

        self.back_button = ctk.CTkButton(self.formCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.place(relx=0.01, rely=0.01, anchor=ctk.NW)


    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()

    def add_action(self):
        insertBook(self.cursor, self.ISBN.get(), self.pub_date.get(), self.description.get("1.0", ctk.END).strip(), self.pages_num.get(), self.title.get())
        # insert category??

    
class UpdateBook:
    def __init__(self, app_frame, back_action):
        self.formCard = ctk.CTkFrame(app_frame, width=600, height=500)

        self.title_label = ctk.CTkLabel(self.formCard, text="Update Book", font=ctk.CTkFont("Arial", size=42, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        self.title = ctk.CTkEntry(self.formCard, placeholder_text="Enter book title here", width=400)
        self.title.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.ISBN = ctk.CTkEntry(self.formCard, placeholder_text="Enter ISBN here", width=400)
        self.ISBN.place(relx=0.5, rely=0.28, anchor=ctk.CENTER) 

        self.desc_label = ctk.CTkLabel(self.formCard, text="Description:", font=ctk.CTkFont("Arial", size=14, weight="bold"), text_color="grey")  
        self.desc_label.place(relx=0.24, rely=0.35, anchor=ctk.CENTER)  
        self.description = ctk.CTkTextbox(self.formCard, width=400, height=120, fg_color="#343638", border_color="#565b5e",border_width=2)
        self.description.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        self.cat_label = ctk.CTkLabel(self.formCard, text="Category:", font=ctk.CTkFont("Arial", size=14, weight="bold"), text_color="grey")  
        self.cat_label.place(relx=0.24, rely=0.67, anchor=ctk.CENTER)  
        options = ["Any", "Science", "Adventure", "Philosophy", "Mystery", "History", "Drama", "Romance", "Fantasy"]
        self.category = ctk.CTkComboBox(self.formCard, values=options)
        self.category.place(relx=0.44, rely=0.67, anchor=ctk.CENTER)

        self.pub_date = ctk.CTkEntry(self.formCard, placeholder_text="Enter publication date (YYYY-MM-DD)", width=400)
        self.pub_date.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)  

        self.pages_num = ctk.CTkEntry(self.formCard, placeholder_text="Enter the number of pages", width=400)
        self.pages_num.place(relx=0.5, rely=0.83, anchor=ctk.CENTER)  
        
        self.edit_button = ctk.CTkButton(self.formCard, text="Edit")
        self.edit_button.place(relx=0.5, rely=0.92, anchor=ctk.CENTER)

        self.back_button = ctk.CTkButton(self.formCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.place(relx=0.01, rely=0.01, anchor=ctk.NW)


    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()