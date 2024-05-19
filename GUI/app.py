import pyodbc
import datetime
import customtkinter as ctk
from main_menu import MainMenu
from user import Signup, UpdateUser
from book import AddBook, UpdateBook

# database setup
cnxn_str=("Driver={ODBC Driver 17 for SQL Server};"
          "Server=localhost;"
          "Database=UniversityLibrary;"
          "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
# cursor
mycursor = cnxn.cursor()

# navigation functions
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
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
app = ctk.CTk()
app.title("FCAI Library")
app.geometry("800x600")

main_menu = MainMenu(app, open_signup, open_update_user, open_add_book, open_update_book)
signup = Signup(app, mycursor, back_to_menu)
update_user = UpdateUser(app, mycursor, back_to_menu)
add_book = AddBook(app, mycursor, back_to_menu)
update_book = UpdateBook(app, back_to_menu)

# first page when you open
main_menu.show()

app.mainloop()