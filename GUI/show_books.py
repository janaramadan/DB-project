import customtkinter as ctk

def getBooks(cursor):
    cursor.execute("SELECT * FROM Book")
    books = cursor.fetchall()
    print("Books:")
    for book in books:
        print(book)

class ViewBooks:
    def __init__(self, app_frame, cursor, back_action):
        self.cursor = cursor
        self.displayCard = ctk.CTkScrollableFrame(app_frame, width=600, height=500)

        # display headers
        headers = ["ISBN", "Title", "Year", "# of pages", "Description"]
        for j, header in enumerate(headers):
            header_label = ctk.CTkLabel(self.displayCard, text=header, font=("Arial", 12, "bold"))
            header_label.grid(row=1, column=j, padx=5, pady=5)


        cursor.execute("SELECT ISBN, Title, PublishYear, Pages, Description FROM Book")
        books = cursor.fetchall()
        for i, book in enumerate(books):
            for j, att in enumerate(book):
                att_label = ctk.CTkLabel(self.displayCard, text=att, wraplength=180)
                att_label.grid(row=i+2, column=j, padx=5, pady=5)

        self.back_button = ctk.CTkButton(self.displayCard, text="Back", fg_color="transparent", width=50, command=lambda: back_action(self))
        self.back_button.grid(row=0, column=0, sticky="w", pady=(0, 10))


    def show(self):
        self.displayCard.pack(pady=(50, 0))

    def hide(self):
        self.displayCard.pack_forget()

    def reset(self):
        pass
        # self.title.delete(0, ctk.END)
        # self.ISBN.delete(0, ctk.END)
        # self.description.delete("1.0", ctk.END)
        # self.category.set("Any")
        # self.pub_date.delete(0, ctk.END)
        # self.pages_num.delete(0, ctk.END)