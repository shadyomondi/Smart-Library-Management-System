# member.py
# ----------------------------------------------------------
# Defines the Member class for the Smart Library Management System
# ----------------------------------------------------------

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # List of book titles borrowed

    def borrow_book(self, book):
        """Borrow a book if available"""
        if book.available_copies > 0:
            book.update_copies(-1)
            book.record_borrow()
            self.borrowed_books.append(book.title)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book):
        """Return a borrowed book"""
        if book.title in self.borrowed_books:
            book.update_copies(1)
            self.borrowed_books.remove(book.title)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"Error: '{book.title}' was not borrowed by {self.name}.")

    def display_member_info(self):
        """Display member details and borrowed books"""
        print(f"Member ID: {self.member_id} | Name: {self.name}")
        print("Borrowed Books:", ", ".join(self.borrowed_books) if self.borrowed_books else "None")
