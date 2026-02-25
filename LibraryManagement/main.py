#This is a simple Library Management System (LMS) implemented in Python. It allows you to manage books and users in a library. The system uses classes to represent books and users, and dictionaries to store the records. The program takes input for books and users, and then displays the records. This is a basic implementation & cna be further enhanced with admin panel to add, delete, update records, issue books to users, and track book history.

class book:
    def __init__(self, id, title, author, units):
        self.id = id
        self.title = title
        self.author = author
        self.units = units
        self.available_units = units

class user:
    def __init__(self, id, name, roll_no, email, mobile, semester, department):
        self.id = id
        self.name = name
        self.roll_no = roll_no
        self.email = email
        self.mobile = mobile
        self.semester = semester
        self.department = department


#DICTIONARIES 
books = {}   # key = book_id, value = book object
users = {}   # key = user_id, value = user object


# TAKING BOOK INPUT 
print("Enter details for 3 books:\n")

for i in range(3):
    print(f"\nBook {i+1}")
    id = int(input("Enter Book ID: "))
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    units = int(input("Enter Units: "))

    new_book = book(id, title, author, units)
    books[id] = new_book   # storing in dictionary

print("\nEnter details for 3 users:\n")

for i in range(3):
    print(f"\nUser {i+1}")
    id = int(input("Enter User ID: "))
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    email = input("Enter Email: ")
    mobile = input("Enter Mobile: ")
    sem = int(input("Enter Semester: "))
    dept = input("Enter Department: ")

    new_user = user(id, name, roll, email, mobile, sem, dept)
    users[id] = new_user   # storing in dictionary


print(" BOOK RECORDS ")
for key, value in books.items():
    print(f"ID: {key}, Title: {value.title}, Author: {value.author}, Available: {value.available_units}/{value.units}")

print(" USER RECORDS ")
for key, value in users.items():
    print(f"ID: {key}, Name: {value.name}, Roll No: {value.roll_no}, Email: {value.email}")
