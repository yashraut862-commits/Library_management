# Library Management System

A simple console-based Library Management System built in Python. It allows a librarian to manage a collection of books — adding new books, viewing the catalog, searching for a book, and issuing/returning books — all through a menu-driven command-line interface.

## Features

- **Add Book** – Add a new book to the library with a unique Book ID, name, and author.
- **Display Books** – View all books currently in the library along with their status (Available/Issued).
- **Search Book** – Search for a book by name.
- **Issue Book** – Mark a book as issued to a borrower using its Book ID.
- **Return Book** – Mark an issued book as returned/available again.
- **Exit** – Safely exit the application.

## How It Works

The system stores books in memory as a list of dictionaries, where each book has:

```python
{
    "id": "Book ID",
    "name": "Book Name",
    "author": "Author Name",
    "status": "Available" / "Issued"
}
```

The program runs an infinite loop displaying a menu, takes the user's numeric choice as input, and performs the corresponding action until the user chooses to exit.

## Requirements

- Python 3.x
- No external libraries required (uses only Python's built-in `input()` and `print()`)

## How to Run

1. Save the code in a file named `library_management_system.py`.
2. Open a terminal in the same directory.
3. Run the following command:

```bash
python library_management_system.py
```

4. Follow the on-screen menu to interact with the system.

## Sample Menu

```
===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. Display Books
3. Search Book
4. Issue Book
5. Return Book
6. Exit
```

## Project Structure

```
library-management-system/
│
├── library_management_system.py   # Main application code
├── README.md                      # Project overview and usage instructions
└── statement.md                   # Problem statement and project scope
```

## Limitations & Future Improvements

- Data is stored only in memory and is lost when the program exits (no file/database persistence).
- No user authentication or role-based access (librarian vs. student).
- Book search only matches by exact name (case-insensitive), not partial matches.
- No due dates, fines, or borrower tracking for issued books.
- Could be extended with a GUI or web interface, and persistent storage (e.g., SQLite or a JSON/CSV file).

## Author

Add your name here.

## License

Add a license of your choice (e.g., MIT) here.
