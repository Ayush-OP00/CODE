#This program is dedicated to the creation of library management system where we have three classe :BOOK, BOOK HISTORY, USER 
#This 3 classes will be governed and utilized by Admin class which will be responsible for the management of the library system. The Admin class will have the ability to add books, issue books to users, and manage user information. 
class book:
    def __init__(self, id, title, author, units, available_units):
        self.id = id
        self.title = title
        self.author = author
        self.units = units
        self.available_units = available_units
class book_history:
    def __init__(self, user, book, issue_date, return_date):
        self.user = user
        self.book = book
        self.issue_date = issue_date
        self.return_date = return_date

