import customtkinter as ctk

# add book functions
def insertBook(cursor, isbn, publish_year, description, pages, title):
    cursor.execute(
        "INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (?, ?, ?, ?, ?)",
        (isbn, publish_year, description, pages, title)
    )

def insertCategory(cursor, isbn, name):
    cursor.execute(
        "INSERT INTO BookCategory (ISBN, Name) VALUES (?, ?)",
        (isbn, name)
    )

def insertAuthor(cursor, isbn, author_name):
    cursor.execute("SELECT author_id FROM author WHERE name = ?", (author_name,))
    author = cursor.fetchone()
    
    if author:
        author_id = author[0]
    else:
        # Insert new author
        cursor.execute("INSERT INTO author (Name, PublishedBooks) OUTPUT INSERTED.author_id VALUES (?, ?)", (author_name, 1))
        author_id = cursor.fetchone()[0]

    cursor.execute("INSERT INTO author_book (author_id, isbn) VALUES (?, ?)", (author_id, isbn))

# edit book functions
def get_book(cursor, isbn):
    cursor.execute("""  SELECT Book.ISBN,Book.title, Book.PublishYear, Book.pages, Book.description
                            FROM
                                Book
                            WHERE 
                                Book.ISBN = ?;""", isbn)
    book = cursor.fetchone()
    return book

def updateBook(cursor, isbn, new_publish_year, new_description, new_pages, new_title):
    cursor.execute(
        "UPDATE Book SET PublishYear = ?, Description = ?, Pages = ?, Title = ? WHERE ISBN = ?",
        (new_publish_year, new_description, new_pages, new_title, isbn)
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
        self.ISBN.place(relx=0.5, rely=0.27, anchor=ctk.CENTER) 

        self.desc_label = ctk.CTkLabel(self.formCard, text="Description:", font=ctk.CTkFont("Arial", size=14, weight="bold"), text_color="grey")  
        self.desc_label.place(relx=0.24, rely=0.34, anchor=ctk.CENTER)  
        self.description = ctk.CTkTextbox(self.formCard, width=400, height=120, fg_color="#343638", border_color="#565b5e",border_width=2)
        self.description.place(relx=0.5, rely=0.49, anchor=ctk.CENTER)
        
        self.cat_label = ctk.CTkLabel(self.formCard, text="Category:", font=ctk.CTkFont("Arial", size=14, weight="bold"), text_color="grey")  
        self.cat_label.place(relx=0.24, rely=0.66, anchor=ctk.CENTER)  
        options = ["Any", "Science", "Adventure", "Philosophy", "Mystery", "History", "Drama", "Romance", "Fantasy"]
        self.category = ctk.CTkComboBox(self.formCard, values=options)
        self.category.place(relx=0.44, rely=0.66, anchor=ctk.CENTER)

        self.author = ctk.CTkEntry(self.formCard, placeholder_text="Enter author name", width=400)
        self.author.place(relx=0.5, rely=0.74, anchor=ctk.CENTER)  

        self.pub_date = ctk.CTkEntry(self.formCard, placeholder_text="Enter publication date (YYYY-MM-DD)", width=400)
        self.pub_date.place(relx=0.5, rely=0.81, anchor=ctk.CENTER)  

        self.pages_num = ctk.CTkEntry(self.formCard, placeholder_text="Enter the number of pages", width=400)
        self.pages_num.place(relx=0.5, rely=0.88, anchor=ctk.CENTER)  
        
        self.add_button = ctk.CTkButton(self.formCard, text="Add", command=self.add_action)
        self.add_button.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

        self.back_button = ctk.CTkButton(self.formCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.place(relx=0.01, rely=0.01, anchor=ctk.NW)


    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()

    def reset(self):
        self.title.delete(0, ctk.END)
        self.ISBN.delete(0, ctk.END)
        self.description.delete("1.0", ctk.END)
        self.category.set("Any")
        self.pub_date.delete(0, ctk.END)
        self.pages_num.delete(0, ctk.END)

    def add_action(self):
        insertBook(self.cursor, self.ISBN.get(), self.pub_date.get(), self.description.get("1.0", ctk.END).strip(), self.pages_num.get(), self.title.get())
        insertCategory(self.cursor,self.ISBN.get() , self.category.get())
        insertAuthor(self.cursor,self.ISBN, self.author.get())
        self.cursor.commit()
        self.reset()

    
class UpdateBook:
    def __init__(self, app_frame, cursor, back_action):
        self.cursor = cursor
        self.formCard = ctk.CTkFrame(app_frame, width=600, height=500)
        
        title_label = ctk.CTkLabel(self.formCard, text="Update Book", font=ctk.CTkFont("Arial", size=42, weight="bold"))
        title_label.place(relx=0.5, rely=0.15, anchor=ctk.CENTER)  

        self.ISBN = ctk.CTkEntry(self.formCard, placeholder_text="Enter the ISBN of an existing book", width=400)
        self.ISBN.place(relx=0.5, rely=0.48, anchor=ctk.CENTER)

        self.title = 1
        self.description = 2
        self.category = 3
        self.pub_date = 4
        self.author = 5
        self.pages_num = 6


        self.confirm= ctk.CTkButton(self.formCard, text="Confirm", command=self.show_details)
        self.confirm.place(relx=0.5, rely=0.63, anchor=ctk.CENTER)
        
        self.back = back_action
        back_button = ctk.CTkButton(self.formCard, text="Back", fg_color="transparent", width=50, command=lambda: self.back(self))
        back_button.place(relx=0.01, rely=0.01, anchor=ctk.NW)

    def show_details(self):
        error_msg = ctk.CTkLabel(self.formCard, text="Book Not Found!", font=ctk.CTkFont("Arial", size=14, weight="bold"))
        isbn_value = self.ISBN.get()
        book = get_book(self.cursor,isbn_value)
        if book:
            if error_msg:
                error_msg.destroy()
                
            self.ISBN.destroy()
            self.confirm.destroy()
            
            self.title = ctk.CTkEntry(self.formCard,  width=400)
            self.title.insert(0, book[1])
            self.title.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)  

            desc_label = ctk.CTkLabel(self.formCard, text="Description:", font=ctk.CTkFont("Arial", size=14, weight="bold"), text_color="grey")  
            desc_label.place(relx=0.24, rely=0.4, anchor=ctk.CENTER)  
            self.description = ctk.CTkTextbox(self.formCard, width=400, height=120, fg_color="#343638", border_color="#565b5e",border_width=2)
            self.description.insert("1.0", book[4])
            self.description.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)  


            self.pub_date = ctk.CTkEntry(self.formCard, placeholder_text="Enter publication date (YYYY-MM-DD)", width=400)
            self.pub_date.insert(0, book[2])
            self.pub_date.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)
            

            self.pages_num = ctk.CTkEntry(self.formCard, placeholder_text="Enter the number of pages", width=400)
            self.pages_num.insert(0, book[3])
            self.pages_num.place(relx=0.5, rely=0.85, anchor=ctk.CENTER)
            

            edit_button = ctk.CTkButton(self.formCard, text="Edit", command=lambda: self.edit_action(isbn_value))
            edit_button.place(relx=0.5, rely=0.92, anchor=ctk.CENTER)  
        else:
            error_msg.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)  
        

    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()

    def reset(self):
        self.title.delete(0, ctk.END)
        self.description.delete("1.0", ctk.END)
        self.pub_date.delete(0, ctk.END)
        self.pages_num.delete(0, ctk.END)

    def edit_action(self, isbn):
        updateBook(self.cursor, isbn, self.pub_date.get(), self.description.get("1.0", ctk.END).strip(),self.pages_num.get(), self.title.get())
        self.cursor.commit()
        self.reset()