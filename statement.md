# Problem Statement

## Problem Statement

Manual/paper-based tracking of library books is time-consuming and error-prone. Librarians often struggle to keep an accurate, up-to-date record of which books are available, which ones have been issued, and to know quickly whether a specific book exists in the collection. There is a need for a simple, lightweight system that lets a librarian manage the core day-to-day operations of a library — adding books, viewing the catalog, searching, issuing, and returning books — without the overhead of a complex software system.

## Scope of the Project

This project implements a **console-based Library Management System** in Python that covers the core operations of managing a small library's book inventory. The scope includes:

- Adding new books to the library catalog.
- Viewing the complete list of books along with their availability status.
- Searching for a book by name.
- Issuing a book to a borrower (marking it as "Issued").
- Returning a previously issued book (marking it as "Available").
- Basic input validation for menu choices.

**Out of scope** for the current version:
- Persistent storage (data resets each time the program restarts).
- Borrower/member management (names, contact details, borrowing history).
- Due dates, overdue tracking, or fine calculation.
- User authentication or multi-user roles.
- A graphical or web-based user interface.

## Target Users

- **Librarians / Library Staff** – to manage the book catalog and track issued/returned books.
- **Small institutions or personal collections** – such as school libraries, small community libraries, or individuals wanting to track their personal book collection, where a lightweight tool is sufficient.
- **Students/Developers** – as a learning project to understand basic CRUD-style operations, control flow, and data structures in Python.

## High-Level Features

1. **Add Book** – Register a new book with a unique ID, name, and author; defaults to "Available" status.
2. **Display Books** – List all books in the system with their ID, name, author, and current status.
3. **Search Book** – Look up a book by its name and display its details if found.
4. **Issue Book** – Change a book's status to "Issued" if it is currently available.
5. **Return Book** – Change a book's status back to "Available" if it was issued.
6. **Menu-Driven Navigation** – A simple, repeating text menu with input validation guides the user through all operations until they choose to exit.
