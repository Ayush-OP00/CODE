#This program is dedicated to the creation of library management system where we have three classe :BOOK, BOOK HISTORY, USER 
class book:
    def __init__(self, id, title, author, units, available_units):
        self.id = id
        self.title = title
        self.author = author
        self.units = units
        self.available_units = available_units
