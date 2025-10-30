# library.py
# ----------------------------------------------------------
# Enhanced version: includes transaction logging (transactions.txt)
# ----------------------------------------------------------

from book import Book
from member import Member
from datetime import datetime
import os

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transaction_history = []
        self.load_books()
        self.load_members()

    # ---------------- FILE HANDLING ----------------
    def load_books(self):
        if os.path.exists("books.txt"):
            with open("books.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if len(data) == 5:
                        book_id, title, author, available_copies, borrow_count = data
                        self.books.append(Book(book_id, title, author, int(available_copies)))
                        self.books[-1].borrow_count = int(borrow_count)

    def save_books(self):
        with open("books.txt", "w") as f:
            for b in self.books:
                f.write(f"{b.book_id},{b.title},{b.author},{b.available_copies},{b.borrow_count}\n")

    def load_members(self):
        if os.path.exists("members.txt"):
            with open("members.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if len(data) >= 2:
                        member_id = data[0]
                        name = data[1]
                        borrowed_books = data[2:] if len(data) > 2 else []
                        member = Member(member_id, name)
                        member.borrowed_books = borrowed_books
                        self.members.append(member)

    def save_members(self):
        with open("members.txt", "w") as f:
            for m in self.members:
                borrowed = ",".join(m.borrowed_books)
                f.write(f"{m.member_id},{m.name}")
                if borrowed:
                    f.write(f",{borrowed}")
                f.write("\n")

    # ---------------- TRANSACTION LOGGING ----------------
    def log_transaction(self, action):
        """Record transactions with timestamp in transactions.txt"""
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_entry = f"{timestamp} {action}\n"
        with open("transactions.txt", "a") as log_file:
            log_file.write(log_entry)

    # ---------------- BOOK MANAGEMENT ----------------
    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' added successfully and saved to file.")
        self.log_transaction(f"Added book '{book.title}' by {book.author}")

    def display_all_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                book.display_info()

    def search_by_author(self, author_name):
        found_books = [b for b in self.books if b.author.lower() == author_name.lower()]
        if found_books:
            print(f"Books by {author_name}:")
            for book in found_books:
                book.display_info()
        else:
            print(f"No books found by {author_name}.")

    # ---------------- MEMBER MANAGEMENT ----------------
    def add_member(self, member):
        self.members.append(member)
        self.save_members()
        print(f"Member '{member.name}' added successfully and saved to file.")
        self.log_transaction(f"Registered new member '{member.name}'")

    def display_all_members(self):
        if not self.members:
            print("No members registered.")
        else:
            for member in self.members:
                member.display_member_info()

    # ---------------- TRANSACTIONS ----------------
    def borrow_transaction(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.title.lower() == book_title.lower()), None)

        if member and book:
            member.borrow_book(book)
            self.transaction_history.append(f"{member.name} borrowed '{book.title}'")
            self.save_books()
            self.save_members()
            self.log_transaction(f"Member {member.name} borrowed '{book.title}'")
        else:
            print("Invalid member ID or book title.")

    def return_transaction(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.title.lower() == book_title.lower()), None)

        if member and book:
            member.return_book(book)
            self.transaction_history.append(f"{member.name} returned '{book.title}'")
            self.save_books()
            self.save_members()
            self.log_transaction(f"Member {member.name} returned '{book.title}'")
        else:
            print("Invalid member ID or book title.")

    # ---------------- REPORTS ----------------
    def most_borrowed_book(self):
        if not self.books:
            print("No books in library.")
            return
        most_borrowed = max(self.books, key=lambda b: b.borrow_count, default=None)
        print(f"Most Borrowed Book: '{most_borrowed.title}' by {most_borrowed.author} ({most_borrowed.borrow_count} times)")

    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("=== TRANSACTION HISTORY ===")
            for record in self.transaction_history:
                print(record)
