USE UniversityLibrary;
GO

-- TABLE CREATION


CREATE TABLE Admin (
    Admin_ID BIGINT NOT NULL PRIMARY KEY,
    Password VARCHAR(50) NOT NULL,
    Username VARCHAR(20) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Country VARCHAR(20) NOT NULL,
    City VARCHAR(20) NOT NULL,
    Street VARCHAR(20) NOT NULL
);


CREATE TABLE Author (
    Author_ID BIGINT NOT NULL PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    PublishedBooks INT NOT NULL
);


CREATE TABLE Book (
    ISBN BIGINT NOT NULL PRIMARY KEY,
    PublishYear DATE NOT NULL,
    Description VARCHAR(50) NOT NULL,
    Pages INT NOT NULL,
    Title VARCHAR(20) NOT NULL
);


CREATE TABLE Student (
    Student_ID BIGINT NOT NULL PRIMARY KEY,
    Password VARCHAR(50) NOT NULL,
    Username VARCHAR(20) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Country VARCHAR(20) NOT NULL,
    City VARCHAR(20) NOT NULL,
    Street VARCHAR(20) NOT NULL
);

-- BorrowedBook table with foreign keys 

CREATE TABLE BorrowedBook (
    Borrowed_ID INT NOT NULL PRIMARY KEY,
    Student_ID BIGINT, -- mesh lazem kol student yekon 3ando borrowed book
    ISBN BIGINT NOT NULL, -- kol borrowed book lazem yekon ketab
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
    FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);

-- BookCategory table --> weak entity with a composite primary key
CREATE TABLE BookCategory (
    ISBN BIGINT NOT NULL,
    Name VARCHAR(50) NOT NULL,
    PRIMARY KEY (ISBN, Name),
    FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);


-- Write relationship
CREATE TABLE Author_Book (
    Author_ID BIGINT NOT NULL,
    ISBN BIGINT NOT NULL,
    PRIMARY KEY (Author_ID, ISBN),
    FOREIGN KEY (Author_ID) REFERENCES Author(Author_ID),
    FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);

-- El insert statements

INSERT INTO Admin (Admin_ID, Password, Username, Email, Country, City, Street) VALUES
(1, 'adminpass', 'admin', 'admin@example.com', 'EGYPT', 'Cairo', '123 Street');

INSERT INTO Student (Student_ID, Password, Username, Email, Country, City, Street) VALUES 
(1, 'studentpass', 'student1', 'student1@example.com', 'EGYPT', 'Giza', '456 Street');


INSERT INTO Author (Author_ID, Name, PublishedBooks) VALUES 
(1, 'AuthorName', 5);


INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES 
(1234567890, '2024-01-01', 'Book Description', 300, 'Book Title');


INSERT INTO BookCategory (ISBN, Name) VALUES 
(1234567890, 'Horror');


INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES 
(1, 1, 1234567890);


INSERT INTO Author_Book (Author_ID, ISBN) VALUES 
(1, 1234567890);

-- EL Select statements

SELECT * FROM Admin;
SELECT * FROM BookCategory;
SELECT * FROM Author;
SELECT * FROM Book;
SELECT * FROM Student;

-- Select Borrowed Books and Student and Book details
SELECT bb.Borrowed_ID, bb.Student_ID, s.Username AS StudentName, bb.ISBN, b.Title AS BookTitle
FROM BorrowedBook bb
JOIN Student s ON bb.Student_ID = s.Student_ID
JOIN Book b ON bb.ISBN = b.ISBN;

-- Select relationship between Author and Book
SELECT ab.Author_ID, a.Name AS AuthorName, ab.ISBN, b.Title AS BookTitle
FROM Author_Book ab
JOIN Author a ON ab.Author_ID = a.Author_ID
JOIN Book b ON ab.ISBN = b.ISBN;

-- Select relationship between Book and Book Category
SELECT bc.ISBN, b.Title AS BookTitle, bc.Name AS CategoryName
FROM BookCategory bc
JOIN Book b ON bc.ISBN = b.ISBN;


--Delete Statments
DELETE FROM Admin
WHERE Email = "admin@example.com";

DELETE FROM BorrowedBook
WHERE Student_ID = 1 AND ISBN = 1234567890;


--Update Statments
UPDATE Admin
SET Email = 'newadmin@example.com'
WHERE Admin_ID = 1;

UPDATE Book
SET Description = 'Updated Book Description'
WHERE ISBN = 1234567890;

