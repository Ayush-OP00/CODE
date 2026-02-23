#This program is dedicated to the creation of library management system where we have three classe :BOOK, BOOK HISTORY, USER 
#This 3 classes will be governed and utilized by Admin class which will be responsible for the management of the library system. The Admin class will have the ability to add books, issue books to users, and manage user information. 
from turtle import title


class book:
    def __init__(self, id, title, author, units, available_units):
        self.id = id
        self.title = title
        self.author = author
        self.units = units
        self.available_units = available_units
class book_history:
    def __init__(self, user, id, book, issue_date, return_date):
        self.user = user
        self.id = id
        self.book = book
        self.issue_date = issue_date
        self.return_date = return_date
class user:
    def __init__(self, id, name, roll_no, email, mobile, semester, department):
        self.id = id
        self.name = name
        self.roll_no = roll_no
        self.email = email
        self.mobile = mobile
        self.semester = semester
        self.department = department
class admin:
    def __init__(self):
        self.books = []
        self.users = []
        self.book_history = []
        self.issued_books = {}  
        def add_book(self, id, title, author, units):
            new_book = book(id, title, author, units, available_units=units)
            self.books.append(new_book)
        def add_user(self, id, name, roll_no, email, mobile, semester, department):
            new_user = user(id, name, roll_no, email, mobile, semester, department)
            self.users.append(new_user)
class admin:
    def __init__(self):
        self.books = []  # List of books
        self.users = []  # List of users
        self.book_history = []  # List of book transactions
        self.issued_books = {}  # Dictionary to track issued books: {user_id: [book_ids]}
    
    def add_book(self, id, title, author, units):
        """Add a new book to the library"""
        new_book = book(id, title, author, units, available_units=units)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")
        return True
    
    def add_user(self, id, name, roll_no, email, mobile, semester, department):
        """Add a new user to the library"""
        new_user = user(id, name, roll_no, email, mobile, semester, department)
        self.users.append(new_user)
        print(f"User '{name}' added successfully!")
        return True   
    def display_books(self):
        """Display all books in the library"""
        if not self.books:
            print("No books available in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Units: {book.units}, Available Units: {book.available_units}")