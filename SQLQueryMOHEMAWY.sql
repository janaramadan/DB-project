USE UniversityLibrary;
GO



-- TABLESS CREATION
CREATE TABLE Admin (
    Admin_ID BIGINT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Password VARCHAR(50) NOT NULL,
    Username VARCHAR(20) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Country VARCHAR(20) NOT NULL,
    City VARCHAR(20) NOT NULL,
    Street VARCHAR(20) NOT NULL
);


CREATE TABLE Author (
    Author_ID BIGINT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    PublishedBooks INT NOT NULL
);


CREATE TABLE Book (
    ISBN BIGINT NOT NULL PRIMARY KEY,
    PublishYear DATE NOT NULL,
    Description VARCHAR(255) NOT NULL,
    Pages INT NOT NULL,
    Title VARCHAR(80) NOT NULL
);


CREATE TABLE Student (
    Student_ID BIGINT IDENTITY(1,1) NOT NULL PRIMARY KEY,
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


-- EL relationship
CREATE TABLE Author_Book (
    Author_ID BIGINT NOT NULL,
    ISBN BIGINT NOT NULL,
    PRIMARY KEY (Author_ID, ISBN),
    FOREIGN KEY (Author_ID) REFERENCES Author(Author_ID),
    FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);


-- El insert statements


--INSERT FEL ADMIN
INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES ('adminpass1', 'Jana', 'admin1@example.com', 'Egypt', 'Cairo', '123 Street');
INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES ('adminpass2', 'Farida', 'admin2@example.com', 'Egypt', 'Alexandria', '456 Street');
INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES ('adminpass3', 'Omar', 'admin3@example.com', 'Egypt', 'Giza', '789 Street');
INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES ('adminpass4', 'Ziad', 'admin4@example.com', 'Egypt', 'Mansoura', '10 Street');
INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES ('adminpass5', 'Khamis', 'admin5@example.com', 'Egypt', 'Aswan', '11 Street');
INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES ('adminpass6', 'Ibrahem', 'admin6@example.com', 'Egypt', 'Luxor', '12 Street');
INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES ('adminpass7', 'admin7', 'admin7@example.com', 'Egypt', 'Suez', '13 Street');
INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES ('adminpass8', 'admin8', 'admin8@example.com', 'Egypt', 'Ismailia', '14 Street');
INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES ('adminpass9', 'admin9', 'admin9@example.com', 'Egypt', 'Fayoum', '15 Street');
INSERT INTO Admin (Password, Username, Email, Country, City, Street) VALUES ('adminpass10', 'admin10', 'admin10@example.com', 'Egypt', 'Hurghada', '16 Street');



--INSERT FEL AUTHOR 
INSERT INTO Author (Name, PublishedBooks) VALUES ('J.K. Rowling', 7);
INSERT INTO Author (Name, PublishedBooks) VALUES ('George R.R. Martin', 5);
INSERT INTO Author (Name, PublishedBooks) VALUES ('Agatha Christie', 66);
INSERT INTO Author ( Name, PublishedBooks) VALUES ('J.R.R. Tolkien', 4);
INSERT INTO Author (Name, PublishedBooks) VALUES ('Stephen King', 63);
INSERT INTO Author (Name, PublishedBooks) VALUES ('Isaac Asimov', 31);
INSERT INTO Author (Name, PublishedBooks) VALUES ('Jane Austen', 6);
INSERT INTO Author (Name, PublishedBooks) VALUES ('Mark Twain', 28);
INSERT INTO Author (Name, PublishedBooks) VALUES ('Ernest Hemingway', 9);
INSERT INTO Author (Name, PublishedBooks) VALUES ('Charles Dickens', 15);



--INSERT FEL BOOK 
INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (9780439708180, '1997-06-26', 'A young boy discovers he is a wizard on his 11th birthday and attends Hogwarts School of Witchcraft and Wizardry.', 320, 'Harry Potter and the Sorcerer Stone');
INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (9780553103540, '1996-08-06', 'Noble families vie for control of the Iron Throne in the fantastical land of Westeros.', 694, 'A Game of Thrones');
INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (9780525478812, '2012-01-10', 'A heart-wrenching story about two teenagers, Hazel and Gus, who meet and fall in love at a cancer support group.', 313, 'The Fault in Our Stars');
INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (9780451524935, '1949-06-08', 'A dystopian novel about a totalitarian regime that uses surveillance and mind control to maintain power.', 328, '1984');
INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (9781503290563, '1813-01-28', 'The romantic clash between the opinionated Elizabeth Bennet and her proud beau, Mr. Darcy.', 279, 'Pride and Prejudice');
INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (9780547928227, '1937-09-21', 'Bilbo Baggins embarks on an unexpected journey to reclaim a treasure guarded by a dragon.', 310, 'The Hobbit');
INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (9780743273565, '1925-04-10', 'A mysterious millionaire obsession with a former lover leads to tragedy.', 180, 'The Great Gatsby');
INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (9780061120053, '1900-05-22', 'A young boy discovers a mysterious world hidden beneath the streets of London and encounters magical creatures.', 372, 'Neverwhere');
INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (9780199232765, '1869-01-01', 'A sweeping epic of Russian society during the Napoleonic Wars.', 1225, 'War and Peace');
INSERT INTO Book (ISBN, PublishYear, Description, Pages, Title) VALUES (9780316769488, '1951-07-16', 'A teenage boy recounts his experiences in New York City after being expelled from prep school.', 214, 'The Catcher in the Rye');




--INSERT FEL STUDENT 
INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES ('studentpass1', 'Jana', 'student1@example.com', 'Egypt', 'Cairo', '1 Street');
INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES ('studentpass2', 'Farida', 'student2@example.com', 'Egypt', 'Alexandria', '2 Street');
INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES ('studentpass3', 'Omar', 'student3@example.com', 'Egypt', 'Giza', '3 Street');
INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES ('studentpass4', 'Ziad', 'student4@example.com', 'Egypt', 'Mansoura', '4 Street');
INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES ('studentpass5', 'Ibrahem', 'student5@example.com', 'Egypt', 'Aswan', '5 Street');
INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES ('studentpass6', 'Khamis', 'student6@example.com', 'Egypt', 'Luxor', '6 Street');
INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES ('studentpass7', 'student7', 'student7@example.com', 'Egypt', 'Suez', '7 Street');
INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES ('studentpass8', 'student8', 'student8@example.com', 'Egypt', 'Ismailia', '8 Street');
INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES ('studentpass9', 'student9', 'student9@example.com', 'Egypt', 'Fayoum', '9 Street');
INSERT INTO Student (Password, Username, Email, Country, City, Street) VALUES ('studentpass10', 'student10', 'student10@example.com', 'Egypt', 'Hurghada', '10 Street');



--INSERT FEL BORROWEDBOOKS
INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (1, 1, 9780439708180);
INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (2, 2, 9780553103540);
INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (3, 3, 9780525478812);
INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (4, 4, 9780451524935);
INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (5, 5, 9781503290563);
INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (6, 6, 9780547928227);
INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (7, 7, 9780743273565);
INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (8, 8, 9780061120053);
INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (9, 9, 9780199232765);
INSERT INTO BorrowedBook (Borrowed_ID, Student_ID, ISBN) VALUES (10, 10, 9780316769488);





--INSERT FEL BOOKCATEGORY 
INSERT INTO BookCategory (ISBN, Name) VALUES (9780439708180, 'Mystery');
INSERT INTO BookCategory (ISBN, Name) VALUES (9780553103540, 'Fantasy');
INSERT INTO BookCategory (ISBN, Name) VALUES (9780525478812, 'Drama');
INSERT INTO BookCategory (ISBN, Name) VALUES (9780451524935, 'History');
INSERT INTO BookCategory (ISBN, Name) VALUES (9781503290563, 'Sci-Fi');
INSERT INTO BookCategory (ISBN, Name) VALUES (9780547928227, 'Romance');
INSERT INTO BookCategory (ISBN, Name) VALUES (9780743273565, 'Horror');
INSERT INTO BookCategory (ISBN, Name) VALUES (9780061120053, 'Science');
INSERT INTO BookCategory (ISBN, Name) VALUES (9780199232765, 'Adventure');
INSERT INTO BookCategory (ISBN, Name) VALUES (9780316769488, 'Philosophy');




--INSERT FEL AUTHORBOOK
INSERT INTO Author_Book (Author_ID, ISBN) VALUES (1, 9780439708180);
INSERT INTO Author_Book (Author_ID, ISBN) VALUES (2, 9780553103540);
INSERT INTO Author_Book (Author_ID, ISBN) VALUES (3, 9780525478812);
INSERT INTO Author_Book (Author_ID, ISBN) VALUES (4, 9780451524935);
INSERT INTO Author_Book (Author_ID, ISBN) VALUES (5, 9781503290563);
INSERT INTO Author_Book (Author_ID, ISBN) VALUES (6, 9780547928227);
INSERT INTO Author_Book (Author_ID, ISBN) VALUES (7, 9780743273565);
INSERT INTO Author_Book (Author_ID, ISBN) VALUES (8, 9780061120053);
INSERT INTO Author_Book (Author_ID, ISBN) VALUES (9, 9780199232765);
INSERT INTO Author_Book (Author_ID, ISBN) VALUES (10, 9780316769488);





-- EL Select statements

SELECT * FROM Admin;
SELECT * FROM Student;
SELECT * FROM BookCategory;
SELECT * FROM Author;
SELECT * FROM Author_Book
SELECT * FROM Book;


-- Select Borrowed Books W Student W Book details
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