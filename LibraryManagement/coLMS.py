#This program is dedicated to the creation of library management system where we have three classes: BOOK, BOOK HISTORY, USER 
#These 3 classes will be governed and utilized by Admin class which will be responsible for the management of the library system. 
# The Admin class will have the ability to add books, issue books to users, and manage user information. 

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
    
    def issue_book(self, user_id, book_id, issue_date, return_date):
        """Issue a book to a user"""
        # Check if user exists
        user_found = False
        for user_obj in self.users:
            if user_obj.id == user_id:
                user_found = True
                break
        
        if not user_found:
            print(f"User with ID {user_id} not found!")
            return False
        
        # Check if book exists and has available units
        book_found = False
        for book_obj in self.books:
            if book_obj.id == book_id:
                book_found = True
                if book_obj.available_units > 0:
                    # Issue the book
                    book_obj.available_units -= 1
                    
                    # Add to dictionary
                    if user_id not in self.issued_books:
                        self.issued_books[user_id] = []
                    self.issued_books[user_id].append(book_id)
                    
                    # Add to book history
                    history = book_history(user_id, book_id, book_obj.title, issue_date, return_date)
                    self.book_history.append(history)
                    
                    print(f"Book '{book_obj.title}' issued to User ID {user_id}")
                    return True
                else:
                    print(f"Book '{book_obj.title}' is not available!")
                    return False
        
        if not book_found:
            print(f"Book with ID {book_id} not found!")
            return False
    
    def display_books(self):
        """Display all books in the library"""
        print("\n=== Books in Library ===")
        for b in self.books:
            print(f"ID: {b.id}, Title: {b.title}, Author: {b.author}, Available: {b.available_units}/{b.units}")
    
    def display_users(self):
        """Display all users"""
        print("\n=== Users in Library ===")
        for u in self.users:
            print(f"ID: {u.id}, Name: {u.name}, Roll No: {u.roll_no}, Email: {u.email}")
    
    def display_issued_books(self):
        """Display issued books using dictionary"""
        print("\n=== Issued Books (Dictionary View) ===")
        for user_id, book_ids in self.issued_books.items():
            print(f"User ID {user_id}: Books issued = {book_ids}")