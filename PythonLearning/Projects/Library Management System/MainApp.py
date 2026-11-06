
'''def main():
    santaclara = Library()
    def mainLibApp():

        while True:
            print("\n Welcome to the Library Management System")
            print("1. User Management")
            print("2. Book Management")
            print("3. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Under User Management: ")
                print("1. Register New Members ")
                print("2. See List of All Members")
                print("3. Search Member by Name/ID")
                nextchoice = int(input("Enter your choice: "))
                if nextchoice == 1:
                    santaclara.register

            elif choice == 2:
                print("Under Book Management: ")
                print("1. Add books")
                print("2. Update Books")
                print("3. Search for a book by title")
                nextchoice = int(input("Enter your choice: "))
            elif choice == 3:
                print("Thank you !!!")
                break

    if __name__ == "__main__":
        mainLibApp()
        '''
# from (file name) import (class name) - format for importing files
from Book import Book
from Library import Library
from Member import Member

#practice
library1 = Library()
book1 = Book("Harry Potter" , "JK Rowling" , 123456)
member1 = Member("Shravya" , 1)
member2 = Member("Sky" , 2)


library1.register_member(member1)
library1.register_member(member2)

library1.add_book(book1)
library1.list_books()
library1.issue_books(member1.member_id,book1.isbn)
library1.return_books(member1.member_id, book1.isbn)

def main():
    isbn_number = 0
    member_id = 0
    library = Library()
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Register Member")
        print("3. List Books")
        print("4. List Members")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_title = input("Enter the book title: ")
            author_name = input("Enter the name of the author: ")
            isbn_number = isbn_number + 1
            isbn = "SCL" + str(isbn_number)
            book = Book(book_title, author_name, isbn)
            library.add_book(book)
        elif choice == 2:
            name = input("Enter your name: ")
            member_id = member_id + 1
            member = Member(name, member_id)
            library.register_member(member)
        elif choice == 3:
            library.list_books()
        elif choice == 4:
            library.list_members()
        elif choice == 5:
            member_id = input("Enter your member_ID: ")
            isbn_number = input("Enter your ISBN number: ")
            library.issue_books(member_id, isbn_number)
        elif choice == 6:
            member_id = input("Enter your member_ID: ")
            isbn_number = input("Enter your ISBN number: ")
            library.return_books(member_id, isbn_number)
        elif choice == 7:
            print("Thanks for visting. See you!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

