import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#Function to return menu
def show_menu():
    print("Main Menu\n")
    print("1. View Books\n2. View Store Locations\n3. My Account\n4. Exit Program")

    user_input = input('Please enter the number for the option you would like to select: ')
    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        print("\nInvalid Input!\n***Program terminated***\n")
        sys.exit(0)

#Function to return books
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    all_books = _cursor.fetchall()

    print("-- DISPLAYING BOOK RECORDS --\n" )
    for book in all_books:
        book_id = book[0]
        book_name = book[1]
        book_author = book[2]
        book_details = book[3]
        print(f"Book ID:{book_id}\nBook Name: {book_name}\nAuthor: {book_author}\nDetails: {book_details}\n\n")

#Function to return locations
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    all_stores = _cursor.fetchall()

    print(" -- DISPLAYING STORE LOCATIONS --\n")
    for store in all_stores:
        store_id = store[0]
        store_locale = store[1]
        print(f"Store ID: {store_id}\nStore Locale: {store_locale}\n\n")

#Validate user function
def validate_user():
    input_user_id = input('Enter User ID: ')
    try:
        input_user_id = int(input_user_id)
        if input_user_id < 0 or input_user_id > 3:
            print("\nInvalid Input!\n***Program terminated***\n")
            sys.exit(0)
        
        return input_user_id
    
    except ValueError:
        print("\nInvalid User ID!\n***Program terminated***\n")
        sys.exit(0)

#Function to return account menu
def show_account_menu():
    print("Customer Menu\n")
    print("1. Wishlist\n2. Add Book\n3. Main Menu\n")
    
    user_input = input('Please enter the number for the option you would like to select: ')
    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        print("\nInvalid Input!\n***Program terminated***\n")
        sys.exit(0)

#Function to return wishlist 
def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist_items = _cursor.fetchall()

    print("-- DISPLAYING USER's WISHLIST ITEMS --\n")

    for book in wishlist_items:
        book_id = book[3]
        book_name = book[4]
        book_author = book[5]
        print(f"Book ID:{book_id}\nBook Name: {book_name}\nAuthor: {book_author}\n\n")

#Function to return list of books to add to wishlist
def show_books_to_add(_cursor, _user_id):
    _cursor.execute("SELECT book_id, book_name, author, details FROM book " +
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    books_to_add = _cursor.fetchall()

    print("-- DISPLAYING AVAILABLE BOOKS --\n")

    for book in books_to_add:
        book_id = book[0]
        book_name = book[1]
        book_author = book[2]
        book_details = book[3]
        print(f"Book ID:{book_id}\nBook Name: {book_name}\nAuthor: {book_author}\nDetails: {book_details}\n\n")

#Function to add book to wishlist 
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#Connect to database
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("Welcome to the WhatABook Application!\n")

    user_input = 0

    #Call appropriate functions depending on user input
    while user_input != 4:
        user_input = show_menu()
        
        if user_input == 1:
            show_books(cursor)

        if user_input == 2:
            show_locations(cursor)
        
        #account menu
        if user_input == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)
                    book_id = int(input("Enter the book id of the book you want to add to your wishlist: "))
                    add_book_to_wishlist(cursor, my_user_id, book_id)
                    db.commit()
                    print(f"Book ID {book_id} has been added to your wishlist")

                if account_option < 0 or account_option > 3:
                    print("Invalid Option Input! Please Retry\n")

                account_option = show_account_menu()
        
        if user_input < 0 or user_input > 4:
            print("Invalid Option Input! Please Retry\n")

    print("***Program terminated***")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)

finally:
    db.close()