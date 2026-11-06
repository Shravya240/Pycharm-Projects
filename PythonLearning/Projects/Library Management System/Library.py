class Library:
    def __init__(self):
        self.books_list = []     #list- add multiple books objects
        self.members_list = []

    def add_book(self, book):
        self.books_list.append(book)
        print(f"Book '{book.title}' added to library.")

    def register_member(self, member):
        self.members_list.append(member)
        print(f"Member '{member.name}' registered.")

    def return_books(self, member_ID, ISBN):
        member = next((m for m in self.members_list if m.member_id == member_ID), None)
        book = next((b for b in self.books_list if b.isbn == ISBN), None)

        if member and book:
            member.return_book(book)
        else:
            print("Either member or book not found")

    def issue_books(self, member_ID, ISBN):
        member = next((m for m in self.members_list if m.member_id == member_ID), None)
        book = next((b for b in self.books_list if b.isbn == ISBN), None)

        if member and book:
            member.borrow_book(book)
        else:
            print("Either member or book not found.")

    def list_books(self):
        for book in self.books_list:
            print(book)

    def list_members(self):
        for member in self.members_list:
            print(member)

    def member_details(self, name, phone_number):
        pass