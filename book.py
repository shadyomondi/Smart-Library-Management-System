class Book:
    def __init__(self, book_id, title, author, available_copies, borrow_count=0):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.borrow_count = borrow_count

    def display_info(self):
        print(f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Available: {self.available_copies}")

    def update_copies(self, number):
        self.available_copies += number

    def increment_borrow_count(self):
        self.borrow_count += 1