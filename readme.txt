SMART LIBRARY MANAGEMENT SYSTEM
---------------------------------

Developed using Python Object-Oriented Programming.

FEATURES:
- Add, view, and manage books and members.
- Borrow and return books with live availability tracking.
- Persistent data storage in text files (books.txt, members.txt).
- Transaction logging and reporting.
- Search books by author.
- Display the most borrowed book.

HOW TO RUN:
1. Ensure Python 3.x is installed.
2. Place all .py and .txt files in the same directory.
3. Run: python main.py
4. Follow on-screen menu prompts.

FILES:
- book.py       → Book class
- member.py     → Member class
- library.py    → Library management
- main.py       → Menu-driven interface
- books.txt     → Book storage
- members.txt   → Member storage
- transactions.txt → Logs all borrow/return actions

ASSUMPTIONS:
- Each book title is unique.
- Member IDs are unique.
