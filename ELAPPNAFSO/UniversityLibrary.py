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


# EL INSERT FUNCTIONS
def insertStudent(cursor, password, username, email, country, city, street):
    cursor.execute(
        "INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES (?, ?, ?, ?, ?, ?)",
        (password, username, email, country, city, street)
    )

def insertBook(cursor, isbn, publish_year, description, pages, title):
    cursor.execute(
        "INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (?, ?, ?, ?, ?)",
        (isbn, publish_year, description, pages, title)
    )

def insertAdmin(cursor, password, username, email, country, city, street):
    cursor.execute(
        "INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES (?, ?, ?, ?, ?, ?)",
        (password, username, email, country, city, street)
    )

def insertBorrowedBook(cursor, borrowed_id, student_id, isbn):
    cursor.execute(
        "INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (?, ?, ?)",
        (borrowed_id, student_id, isbn)
    )

# EL 2 DELETE FUNCTIONS WITH CONDITIONS
def deleteAdmin(cursor, email):
    cursor.execute(
        "DELETE FROM Admin WHERE Email = ?",
        (email,)
    )

def deleteBorrowedBook(cursor, student_id, isbn):
    cursor.execute(
        "DELETE FROM BorrowedBook WHERE Student_ID = ? AND ISBN = ?",
        (student_id, isbn)
    )


# EL 2 UPDATE FUNCTIONS WITH CONDITIONS
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


#===================================FUNCTIONS NEEDED IN GUI===================================

def insertCategory(cursor, isbn, name):
    cursor.execute(
        "INSERT INTO BookCategory (ISBN, Name) VALUES (?, ?)",
        (isbn, name)
    )

def updateAdmin(cursor, new_username, new_email, new_country, new_city, new_street):
    cursor.execute(
        "UPDATE Admin SET Username = ?, Email = ?, Country = ?, City = ?, Street = ?",
        (new_username, new_email, new_country, new_city, new_street)
    )

def updateStudent(cursor, new_username, new_email, new_country, new_city, new_street):
    cursor.execute(
        "UPDATE Student SET Username = ?, Email = ?, Country = ?, City = ?, Street = ?",
        (new_username, new_email, new_country, new_city, new_street)
    )


def updateBook(cursor, isbn, new_publish_year, new_description, new_pages, new_title):
    cursor.execute(
        "UPDATE Book SET PublishYear = ?, Description = ?, Pages = ?, Title = ? WHERE ISBN = ?",
        (new_publish_year, new_description, new_pages, new_title, isbn)
    )





#SELECT FROM ANY TABLES
def getAdmins(cursor):
    cursor.execute("SELECT * FROM Admin")
    admins = cursor.fetchall()
    print("Admins:")
    for admin in admins:
        print(admin)

def getAuthors(cursor):
    cursor.execute("SELECT * FROM Author")
    authors = cursor.fetchall()
    print("Authors:")
    for author in authors:
        print(author)

def getBooks(cursor):
    cursor.execute("SELECT * FROM Book")
    books = cursor.fetchall()
    print("Books:")
    for book in books:
        print(book)

def getStudents(cursor):
    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()
    print("Students:")
    for student in students:
        print(student)

def getBorrowedBooks(cursor):
    cursor.execute("SELECT * FROM BorrowedBook")
    borrowed_books = cursor.fetchall()
    print("Borrowed Books:")
    for borrowed_book in borrowed_books:
        print(borrowed_book)

def getCategories(cursor):
    cursor.execute("SELECT * FROM BookCategory")
    book_categories = cursor.fetchall()
    print("Book Categories:")
    for book_category in book_categories:
        print(book_category)

def getAuthorBooks(cursor):
    cursor.execute("SELECT * FROM Author_Book")
    author_books = cursor.fetchall()
    print("Author Books:")
    for author_book in author_books:
        print(author_book)




#SELECT FROM TABLE WITH JOINS
def getStudentBorrowedBooks(cursor):
    cursor.execute("""
    SELECT 
        s.Student_ID,
        s.Username AS StudentUsername,
        s.Email AS StudentEmail,
        b.ISBN,
        b.Title,
        bb.Borrowed_ID
    FROM 
        BorrowedBook bb
    JOIN 
        Student s ON bb.Student_ID = s.Student_ID
    JOIN 
        Book b ON bb.ISBN = b.ISBN
    """)
    records = cursor.fetchall()
    print("Student Borrowed Books:")
    for record in records:
        print(record)




# KOL EL TESTS FY FUNCTION WAHDA
def test():
    # insert statments test
    # insertStudent(cursor, '123', 'JanaRamadan', 'JanaRamadan@gmail.com', 'EGYPT', 'Cairo', '123 STREET')
    # insertBook(cursor, 9789876543210, '2003-11-07', 'BOOK DESCRIPTION', 200, 'BOOK TITLE')
    # insertAdmin(cursor, 'pass456', 'faridaaa' , 'farida123@gmail.com', 'EGYPT', 'Cairo', '456 STREET')
    # insertBorrowedBook(cursor, 11, 3, 9789876543210)


    #lazem w ehna ben add BorrowedBook elid yekoon unique w el ISBN beta3 el ketab yekoon mawgood asln
    #el ids beta3t el admin wel student lazem tekoon unique



    # #update statments test
    updateAdminEmail(cursor, 2, 'newemail@admin.com')
    updateBookDescription(cursor, 9789876543210, 'New Description')
    
    #delete statments test
    deleteAdmin(cursor, 'newemail@admin.com')
    deleteBorrowedBook(cursor, 3, 9789876543210)

    insertCategory(cursor, 9780553104540, 'Comedy')
    updateAdmin(cursor, 'NewUsernameADMIN', 'newadmin@example.com', 'Country', 'City', 'NewStreet')
    updateStudent(cursor, 'NewUsernameSTUDENT', 'newstudent@example.com', 'Country', 'City', 'NewStreet')
    updateBook(cursor, 9780061120053, '2024-01-01', 'New Description', 400, 'New Title')


    
    #select functions ba 
    getStudents(cursor)
    getBooks(cursor)
    getAdmins(cursor)
    getAuthors(cursor)
    getBorrowedBooks(cursor)
    getCategories(cursor)
    getAuthorBooks(cursor)
    getStudentBorrowedBooks(cursor)
    insertCategory(cursor)
    updateAdmin(cursor)
    updateStudent(cursor)
    updateBook(cursor)
    




#garab ba
test()

# Zee3 w e2fel
cnxn.commit()
cnxn.close()