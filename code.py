# LIBRARY MANAGEMENT SYSTEM
books = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        book_id = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "name": name,
            "author": author,
            "status": "Available"
        }

        books.append(book)
        print("Book added successfully!")

    elif choice == 2:
        if len(books) == 0:
            print("No books available.")
        else:
            print("\n----- BOOK LIST -----")
            for book in books:
                print("Book ID:", book["id"])
                print("Book Name:", book["name"])
                print("Author:", book["author"])
                print("Status:", book["status"])
                print("--------------------")

    elif choice == 3:
        search = input("Enter Book Name to search: ")
        found = False

        for book in books:
            if book["name"].lower() == search.lower():
                print("\nBook Found!")
                print("Book ID:", book["id"])
                print("Book Name:", book["name"])
                print("Author:", book["author"])
                print("Status:", book["status"])
                found = True

        if not found:
            print("Book not found.")

    elif choice == 4:
        book_id = input("Enter Book ID to issue: ")
        found = False

        for book in books:
            if book["id"] == book_id:
                found = True

                if book["status"] == "Available":
                    book["status"] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")

        if not found:
            print("Book not found.")

    elif choice == 5:
        book_id = input("Enter Book ID to return: ")
        found = False

        for book in books:
            if book["id"] == book_id:
                found = True

                if book["status"] == "Issued":
                    book["status"] = "Available"
                    print("Book returned successfully!")
                else:
                    print("This book was not issued.")

        if not found:
            print("Book not found.")

    elif choice == 6:
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")

end 