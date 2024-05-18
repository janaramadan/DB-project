import customtkinter as ctk
from user import Signup, UpdateUser
from book import AddBook, UpdateBook
from main_menu import MainMenu


def back_to_menu(view):
    view.hide()
    main_menu.show()

def open_signup():
    main_menu.hide()
    signup.show()

def open_update_user():
    main_menu.hide()
    update_user.show()

def open_add_book():
    main_menu.hide()
    add_book.show()

def open_update_book():
    main_menu.hide()
    update_book.show()

# setup
app = ctk.CTk()
app.title("FCAI Library")
app.geometry("800x600")

main_menu = MainMenu(app, open_signup, open_update_user, open_add_book, open_update_book)
signup = Signup(app, back_to_menu)
update_user = UpdateUser(app, back_to_menu)
add_book = AddBook(app, back_to_menu)
update_book = UpdateBook(app, back_to_menu)

# first page when you open
main_menu.show()

app.mainloop()