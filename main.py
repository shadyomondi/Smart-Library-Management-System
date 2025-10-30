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
        print("7. Search Books by Author")
        print("8. Display Most Borrowed Book")
        print("9. Display Transaction History")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            available_copies = int(input("Enter Available Copies: "))
            library.add_book(Book(book_id, title, author, available_copies))
            print("Book added successfully!")

        elif choice == '2':
            member_id = input("Enter Member ID: ")
            name = input("Enter Name: ")
            library.add_member(Member(member_id, name))
            print("Member added successfully!")

        elif choice == '3':
            print("\n--- All Books ---")
            library.display_all_books()

        elif choice == '4':
            print("\n--- All Members ---")
            library.display_all_members()

        elif choice == '5':
            member_id = input("Enter Member ID: ")
            book_title = input("Enter Book Title: ")
            library.borrow_transaction(member_id, book_title)

        elif choice == '6':
            member_id = input("Enter Member ID: ")
            book_title = input("Enter Book Title: ")
            library.return_transaction(member_id, book_title)

        elif choice == '7':
            author_name = input("Enter Author's Name: ")
            library.search_by_author(author_name)

        elif choice == '8':
            library.display_most_borrowed_book()

        elif choice == '9':
            library.display_transaction_history()

        elif choice == '10':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
