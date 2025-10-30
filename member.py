class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            self.borrowed_books.append(book)
            book.update_copies(-1)
            print(f"{self.name} has successfully borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_copies(1)
            print(f"{self.name} has successfully returned {book.title}")
        else:
            print(f"Error: {self.name} did not borrow {book.title}.")

    def display_member_info(self):
        print(f"Member ID: {self.member_id} | Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print("No books borrowed.")