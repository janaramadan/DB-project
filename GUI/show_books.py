import customtkinter as ctk

class ViewBooks:
    def __init__(self, app_frame, cursor, back_action):
        self.cursor = cursor
        self.displayCard = ctk.CTkScrollableFrame(app_frame, width=600, height=500)

        # display headers
        headers = ["ISBN", "Title", "Author", "Category", "Year", "# of pages", "Description"]
        for j, header in enumerate(headers):
            header_label = ctk.CTkLabel(self.displayCard, text=header, font=("Arial", 12, "bold"))
            header_label.grid(row=1, column=j, padx=2, pady=5)

        # get all book details
        cursor.execute("""  SELECT
                                Book.ISBN,
                                Book.title,
                                Author.name,
                                BookCategory.Name,
                                Book.PublishYear,
                                Book.pages,
                                Book.description
                            FROM
                                author_book
                            JOIN 
                                Book ON Author_Book.ISBN = Book.ISBN
                            JOIN
                                Author ON Author_Book.Author_ID = Author.Author_ID
                            JOIN 
                                BookCategory ON BookCategory.ISBN = Book.ISBN;""")
        books = cursor.fetchall()

        # iterating on books
        for i, book in enumerate(books, start=2):
            # iterating on book's attributes
            for j, att in enumerate(book):
                att_label = ctk.CTkLabel(self.displayCard, text=att, wraplength=100)
                att_label.grid(row=i*2, column=j, padx=2, pady=5)
            # Add a separator line below each row
            separator = ctk.CTkLabel(self.displayCard, text="", height=2, width=600, bg_color="gray")
            separator.grid(row=i*2-1, column=0, columnspan=len(headers), sticky="ew", pady=(0, 2))

        self.back_button = ctk.CTkButton(self.displayCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.grid(row=0, column=0, sticky="w", pady=(0, 10))


    def show(self):
        self.displayCard.pack(pady=(50, 0))

    def hide(self):
        self.displayCard.pack_forget()

#################################################################################################################################################

def get_filtered_books(cursor, filter_by, value):
    if filter_by == "Title":
        filter_by = "Book.title"
    elif filter_by == "ISBN":
        filter_by = "Book.ISBN"
    elif filter_by == "Author":
        filter_by = "Author.name"
    elif filter_by == "Year":
        filter_by = "Book.PublishYear"
    elif filter_by == "Category":
        filter_by = "BookCategory.Name"

    cursor.execute(f"""  SELECT
                                Book.ISBN,
                                Book.title,
                                Author.name,
                                BookCategory.Name,
                                Book.PublishYear,
                                Book.pages,
                                Book.description
                            FROM
                                author_book
                            JOIN 
                                Book ON Author_Book.ISBN = Book.ISBN
                            JOIN
                                Author ON Author_Book.Author_ID = Author.Author_ID
                            JOIN 
                                BookCategory ON BookCategory.ISBN = Book.ISBN
                            WHERE {filter_by} = ?;""", (value))
    books = cursor.fetchall()
    return books


class ViewBySearch:
    def __init__(self, app_frame, cursor, back_action):
        self.cursor = cursor

        # A frame for search controls
        self.search_frame = ctk.CTkFrame(app_frame, fg_color="transparent", width=550)

        self.search_bar = ctk.CTkEntry(self.search_frame, placeholder_text="search", width=300)
        self.search_bar.grid(row=0, column=1, )

        options = ["Title", "ISBN", "Author", "Category", "Year"]
        self.search_by = ctk.CTkComboBox(self.search_frame, values=options, width=100)
        self.search_by.grid(row=0, column=2)

        self.search_button = ctk.CTkButton(self.search_frame, text="Search", width=100, command=self.on_search)
        self.search_button.grid(row=0, column=3)

        self.back_button = ctk.CTkButton(self.search_frame, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.grid(row=0, column=0, padx=(10, 20))

        # A scrollable frame for displaying results
        self.displayCard = ctk.CTkScrollableFrame(app_frame, width=600, height=500)

    def show(self):
        self.search_frame.pack(pady=(20, 0))
        self.displayCard.pack(pady=(10, 0))

    def hide(self):
        self.search_frame.pack_forget()
        self.displayCard.pack_forget()

    def on_search(self):
        print(self.search_by.get(), self.search_bar.get())
        result = get_filtered_books(self.cursor, self.search_by.get(), self.search_bar.get())

        if result:
            # Clear previous results
            for widget in self.displayCard.winfo_children():
                widget.destroy()

            # Display headers
            headers = ["ISBN", "Title", "Author", "Category", "Year", "# of pages", "Description"]
            for j, header in enumerate(headers):
                header_label = ctk.CTkLabel(self.displayCard, text=header, font=("Arial", 12, "bold"))
                header_label.grid(row=0, column=j, padx=2, pady=5)

            for i, book in enumerate(result, start=1):
                for j, att in enumerate(book):
                    att_label = ctk.CTkLabel(self.displayCard, text=att, wraplength=100)  # No wraplength for ISBN
                    att_label.grid(row=i, column=j, padx=2, pady=5)

        else:
            print("not found")

