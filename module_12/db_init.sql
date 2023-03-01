-- Anthony Murdock
-- 2/19/2023
-- Database & Table Creation 

USE whatabook;

-- Drop old data
DROP USER IF EXISTS 'whatabook_user'@'localhost';
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;

-- Creating new user 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

 -- Granting privileges to user
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- Creating tables
CREATE TABLE user (
    user_id         INT NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE book (
    book_id     INT NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE store (
    store_id    INT NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE wishlist (
    wishlist_id     INT NOT NULL    AUTO_INCREMENT,
    user_id         INT NOT NULL,
    book_id         INT NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


-- Insertion of data
INSERT INTO user(first_name, last_name) VALUES('Tony', 'Montana');

INSERT INTO user(first_name, last_name) VALUES('John', 'Doe');

INSERT INTO user(first_name, last_name) VALUES('Jane', 'Judy Dench');

INSERT INTO book(book_name, author, details) VALUES('The Adventures of Captain Underpants', 'Dav Pilkey', 'First in the series');

INSERT INTO book(book_name, author, details) VALUES('Captain Underpants and the Attack of the Talking Toilets', 'Dav Pilkey', 'Second in the series');

INSERT INTO book(book_name, author, details) VALUES('Captain Underpants and the Invasion of the Incredibly Naughty Cafeteria Ladies from Outer Space', 'Dav Pilkey', 'Third in the series');

INSERT INTO book(book_name, author, details) VALUES('Captain Underpants and the Perilous Plot of Professor Poopypants', 'Dave Pilkey', 'Fourth in the series');

INSERT INTO book(book_name, author, details) VALUES('Captain Underpants and the Wrath of the Wicked Wedgie Woman', 'Dave Pilkey', 'Fifth in the series');

INSERT INTO book(book_name, author, details) VALUES("Harry Potter and the Philosopher/'s Stone", 'J.K. Rowling', 'First in the series of Harry Potter');

INSERT INTO book(book_name, author, details) VALUES('Harry Potter and the Chamber of Secrets', 'J.K. Rowling', 'Second in the series of Harry Potter');

INSERT INTO book(book_name, author, details) VALUES('THarry Potter and the Prisoner of Azkaban', 'J.K. Rowling', 'Third in the series of Harry Potter');

INSERT INTO book(book_name, author, details) VALUES('Unwind', 'Neal Shusterman', 'Dystopian novel');

INSERT INTO store(locale) VALUES('R. das Carmelitas 144, 4050-161 Porto, Portugal');

INSERT INTO wishlist(user_id, book_id) VALUES ((SELECT user_id FROM user WHERE first_name = 'Tony'), (SELECT book_id FROM book WHERE book_name = 'The Adventures of Captain Underpants'));

INSERT INTO wishlist(user_id, book_id) VALUES ((SELECT user_id FROM user WHERE first_name = 'John'),(SELECT book_id FROM book WHERE book_name = 'Harry Potter and the Chamber of Secrets'));

INSERT INTO wishlist(user_id, book_id) VALUES ((SELECT user_id FROM user WHERE first_name = 'Jane'),(SELECT book_id FROM book WHERE book_name = 'Unwind'));