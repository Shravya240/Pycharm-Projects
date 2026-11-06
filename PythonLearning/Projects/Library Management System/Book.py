'''__init__ :    is a special method within a class,
    often referred to as the initializer method.
    Its primary purpose is to initialize the attributes of an object
    when a new instance of the class is created.'''

'''
    __str__ :     is a special method (also known as a "dunder" method, 
    short for double underscore) that defines the informal, 
    human-readable string representation of an object.
    '''

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

    def book_status(self):
        status = "Available" if self.available else "Not Available"
        return f"(ISBN: {self.isbn}) - {status}"
