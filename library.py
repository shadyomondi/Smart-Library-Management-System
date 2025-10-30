from book import Book
from member import Member
import datetime

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []
        self.load_books()
        self.load_members()
        self.load_transactions()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def add_member(self, member):
        self.members.append(member)
        self.save_members()

    def display_all_books(self):
        for book in self.books:
            book.display_info()

    def display_all_members(self):
        for member in self.members:
            member.display_member_info()

    def find_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_transaction(self, member_id, book_title):
        member = self.find_member(member_id)
        book = self.find_book(book_title)
        if member and book:
            member.borrow_book(book)
            book.increment_borrow_count()
            self.log_transaction(f"Borrowed: {book.title} by {member.name}")
            self.save_books()
            self.save_transactions()
        else:
            print("Error: Member or Book not found.")

    def return_transaction(self, member_id, book_title):
        member = self.find_member(member_id)
        book = self.find_book(book_title)
        if member and book:
            member.return_book(book)
            self.log_transaction(f"Returned: {book.title} by {member.name}")
            self.save_books()
            self.save_transactions()
        else:
            print("Error: Member or Book not found.")

    def log_transaction(self, transaction):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp} - {transaction}")

    def display_transaction_history(self):
        print("\n--- Transaction History ---")
        for transaction in self.transactions:
            print(transaction)

    def search_by_author(self, author_name):
        found_books = False
        print(f"\n--- Books by {author_name} ---")
        for book in self.books:
            if book.author.lower() == author_name.lower():
                book.display_info()
                found_books = True
        if not found_books:
            print(f"No books found by {author_name}.")

    def display_most_borrowed_book(self):
        if not self.books:
            print("No books in the library.")
            return

        most_borrowed = max(self.books, key=lambda book: book.borrow_count)
        if most_borrowed.borrow_count > 0:
            print("\n--- Most Borrowed Book ---")
            most_borrowed.display_info()
            print(f"Borrowed {most_borrowed.borrow_count} times.")
        else:
            print("No books have been borrowed yet.")

    def save_books(self):
        with open("books.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.book_id},{book.title},{book.author},{book.available_copies},{book.borrow_count}\n")

    def load_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    book_id, title, author, available_copies, borrow_count = parts
                    self.books.append(Book(book_id, title, author, int(available_copies), int(borrow_count)))
        except FileNotFoundError:
            pass
        except ValueError:
            # Handle case where borrow_count is not in the file for older data
            with open("books.txt", "r") as file:
                for line in file:
                    book_id, title, author, available_copies = line.strip().split(',')
                    self.books.append(Book(book_id, title, author, int(available_copies)))


    def save_members(self):
        with open("members.txt", "w") as file:
            for member in self.members:
                borrowed_books = ','.join([book.title for book in member.borrowed_books])
                file.write(f"{member.member_id},{member.name},{borrowed_books}\n")

    def load_members(self):
        try:
            with open("members.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    member_id, name = parts[:2]
                    borrowed_books_titles = parts[2:] if len(parts) > 2 else []
                    member = Member(member_id, name)
                    for title in borrowed_books_titles:
                        book = self.find_book(title)
                        if book:
                            member.borrowed_books.append(book)
                    self.members.append(member)
        except FileNotFoundError:
            pass

    def save_transactions(self):
        with open("transactions.txt", "w") as file:
            for transaction in self.transactions:
                file.write(f"{transaction}\n")

    def load_transactions(self):
        try:
            with open("transactions.txt", "r") as file:
                self.transactions = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass
