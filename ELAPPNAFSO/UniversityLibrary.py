import pyodbc
import pandas as pd
import datetime

cnxn_str=("Driver={ODBC Driver 17 for SQL Server};"
          "Server=localhost;"
          "Database=UniversityLibrary;"            #databasebeta3naaa
          "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)


#==================KOL ELY FO2 DA 3ASHAN NE CONNECT BEL DATABASE=======================================

# E3mel el cursor
cursor = cnxn.cursor()

# 2 INSERT FUNCTIONS
def insertStudent(cursor, student_id, password, username, email, country, city, street):
    cursor.execute(
        "INSERT INTO Student (Student_ID, Password, Username, Email, Country, City, Street) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (student_id, password, username, email, country, city, street)
    )

def insertBook(cursor, isbn, publish_year, description, pages, title):
    cursor.execute(
        "INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (?, ?, ?, ?, ?)",
        (isbn, publish_year, description, pages, title)
    )

def insertAdmin(cursor, admin_id, password, username, email, country, city, street):
    cursor.excute(
        "INSERT INTO Admin (Admin_ID, Password, Username, Email, Country, City, Street) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (admin_id, password, username, email, country, city, street)
    )

def insertBorrowedBooks(Borrowed_ID, Student_ID, ISBN):
    cursor.excute(
        "INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (Borrowed_ID, Student_ID, ISBN)
    )

# GARAB BA
insertStudent(cursor, 3, '123', 'Jana', 'Jana@gmail.com', 'EGYPT', 'Cairo', '123 STREET')
insertBook(cursor, 9789876543210, '2003-11-07', 'BOOK DESCRIPTION', 200, 'BOOK TITLE')
insertAdmin(cursor, 2, '456', 'farida' , 'farida@gmail.com', 'EGYPT', 'Cairo', '456 STREET')
insertBorrowedBooks(cursor, 4, 3, 9789876543210)

# 2 UPDATE FUNCTIONS
def updateAdminEmail(cursor, admin_id, new_email):
    cursor.execute(
        "UPDATE Admin SET Email = ? WHERE Admin_ID = ?",
        (new_email, admin_id)
    )

def updateBookDescription(cursor, isbn, new_description):
    cursor.execute(
        "UPDATE Book SET Description = ? WHERE ISBN = ?",
        (new_description, isbn)
    )


def getAllStudents(cursor):
    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()
    print("Students:")
    for student in students:
        print(student)


def getAllBooks(cursor):
    cursor.execute("SELECT * FROM Book")
    books = cursor.fetchall()
    print("Books:")
    for book in books:
        print(book)

def getAllAdmins(cursor):
    cursor.execute("SELECT * FROM Admin")
    admins = cursor.fetchall()
    print("Admins:")
    for admin in admins:
        print(admin)

def getAllBorrowedBooks(cursor):
    cursor.execute("SELECT * FROM BorrowedBooks")
    borrowed_books = cursor.fetchall()
    print("Borrowed Books:")
    for borrowed_book in borrowed_books:
        print(borrowed_book)


# DISPLAY
getAllStudents(cursor)
getAllBooks(cursor)
getAllAdmins(cursor)
getAllBorrowedBooks(cursor)

# ZEE3 W E2FEL
cnxn.commit()
cnxn.close()
