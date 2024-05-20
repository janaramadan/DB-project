import customtkinter as ctk

def book_num(cursor):
    cursor.execute("SELECT COUNT(*) FROM Book")
    books_count = cursor.fetchone()[0]
    return books_count

def student_num(cursor):
    cursor.execute("SELECT COUNT(*) FROM Student")
    students_count = cursor.fetchone()[0]
    return students_count

def admin_num(cursor):
    cursor.execute("SELECT COUNT(*) FROM Admin")
    students_count = cursor.fetchone()[0]
    return students_count

def borrowed_books_num(cursor):
    cursor.execute("SELECT COUNT(*) FROM BorrowedBook")
    borrowed_books_count = cursor.fetchone()[0]
    return borrowed_books_count

def borrowed_books_student(cursor):
    cursor.execute("""
        SELECT s.Student_ID, s.Username, COUNT(*) as TotalBooksBorrowed
        FROM Student s
        JOIN BorrowedBook bb ON s.Student_ID = bb.Student_ID
        GROUP BY s.Student_ID, s.Username
    """)
    records = cursor.fetchall()
    return records

def report(cursor):
    pass
    # print("=== Library Database Report ===")
    # print(f"Books Count: {books_count}")
    # print(f"Students Count: {students_count}")
    # print(f"Borrowed Books Count: {borrowed_books_count}")

    # print("\nTotal number of books borrowed by each student:")
    # for record in records:
    #     print(f"Student ID: {record[0]}, Username: {record[1]}, Total Books Borrowed: {record[2]}")

class Report:
    def __init__(self, app_frame, cursor, back_action):
        self.cursor = cursor
        self.formCard = ctk.CTkScrollableFrame(app_frame, width=600, height=500)

        self.title_label = ctk.CTkLabel(self.formCard, text="Library Database Report", font=ctk.CTkFont("Arial", size=36, weight="bold"))
        self.title_label.pack(pady=(10, 20))

        self.books_num = ctk.CTkLabel(self.formCard, text=f"Number of books: {book_num(self.cursor)}", font=ctk.CTkFont("Arial", size=16))
        self.books_num.pack(pady=(10, 20))

        self.users_num = ctk.CTkLabel(self.formCard, text=f"Number of users: {student_num(self.cursor) + admin_num(self.cursor)}", font=ctk.CTkFont("Arial", size=16))
        self.users_num.pack(pady=(10, 20))

        self.borrowed_books_num = ctk.CTkLabel(self.formCard, text=f"Number of borrowed books: {borrowed_books_num(self.cursor)}", font=ctk.CTkFont("Arial", size=16))
        self.borrowed_books_num.pack(pady=(10, 20))

        self.section_title = ctk.CTkLabel(self.formCard, text="Total number of books borrowed by each student:", font=ctk.CTkFont("Arial", size=24, weight="bold"))
        self.section_title.pack(pady=(10, 20))

        student_borrowed_books = borrowed_books_student(self.cursor)
        for student in student_borrowed_books:
            record = ctk.CTkLabel(self.formCard, text=f"Student ID: {student[0]}, Username: {student[1]}, Total Books Borrowed: {student[2]}", font=ctk.CTkFont("Arial", size=16))
            record.pack(pady=(10, 20))
    
    def show(self):
        self.formCard.pack(pady=(50, 0))

    def hide(self):
        self.formCard.pack_forget()