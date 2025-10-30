# book.py
# ----------------------------------------------------------
# Defines the Book class for the Smart Library Management System
# ----------------------------------------------------------

class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.borrow_count = 0  # Track how many times the book has been borrowed

    def display_info(self):
        """Display detailed book information"""
        print(f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Available Copies: {self.available_copies}")

    def update_copies(self, number):
        """Increase or decrease available copies"""
        self.available_copies += number

    def record_borrow(self):
        """Increment borrow counter for tracking most borrowed books"""
        self.borrow_count += 1
