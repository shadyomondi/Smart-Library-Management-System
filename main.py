# main.py
# ----------------------------------------------------------
# Main program to run the Smart Library Management System
# Provides menu-driven interaction for users
# ----------------------------------------------------------

from library import Library
from book import Book
from member import Member

def main():
    library = Library()

    while True:
        print("\n===== SMART LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add New Book")
        print("2. Add New Member")
        print("3. Display All Books")
        print("4. Display All Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Search by Author")
        print("8. Most Borrowed Book")
        print("9. Transaction History")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            copies = int(input("Enter Available Copies: "))
            library.add_book(Book(book_id, title, author, copies))

        elif choice == '2':
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            library.add_member(Member(member_id, name))

        elif choice == '3':
            library.display_all_books()

        elif choice == '4':
            library.display_all_members()

        elif choice == '5':
            member_id = input("Enter Member ID: ")
            title = input("Enter Book Title: ")
            library.borrow_transaction(member_id, title)

        elif choice == '6':
            member_id = input("Enter Member ID: ")
            title = input("Enter Book Title: ")
            library.return_transaction(member_id, title)

        elif choice == '7':
            author = input("Enter Author Name: ")
            library.search_by_author(author)

        elif choice == '8':
            library.most_borrowed_book()

        elif choice == '9':
            library.show_transaction_history()

        elif choice == '10':
            print("Exiting Smart Library System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
