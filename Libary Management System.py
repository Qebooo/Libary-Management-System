# //pseudocode 
# Library Management System:
# print menu:
    # 1. add book
    # 2. borrow book
    # 3. return book 
    # 4. view books   
    # 6. exit

# 4 view method:
  # Shows books that are available
   # Shows books that are borrowed
    # Shows books that are not available


# 1 add method:
  # Add a book to the library

# 2 borrow method:
  # Borrow a book from the library

# 3 return method:
  # Return a borrowed book to the library
   # Check if the book is borrowed

# 5 exit method:
  # Exit the program


print("1. Add book")
print("2. Borrow book")
print("3. Return book")
print("4. View books")
print("5. Exit")

books = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "available": True},
    {"title": "Percy Jackson", "author": "Rick Riordan", "available": True},
    {"title": "The Hunger Games", "author": "Suzanne Collins", "available": True},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "available": True},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True}
]

while True:
    select = input("Enter your choice: ")
    if select == "4":
        print("In the library we have the following books:")
        for book in books:
            if book["available"]:
                print(f"{book['title']} by {book['author']}")
            else:
                print(f"{book['title']} by {book['author']} (Borrowed)")
    elif select == "1":
        add_book = input("Enter the name of the book you want to add: ")
        add_author = input("Enter the author of the book: ")
        books.append({"title": add_book, "author": add_author, "available": True})
        print(f"Book {add_book} by {add_author} added successfully")
    elif select == "2":
        borrow_book = input("Enter the name of the book you want to borrow: ")
        found = False
        for book in books:
            if book["title"] == borrow_book and book["available"]:
                book["available"] = False
                print(f"Book {borrow_book} borrowed successfully")
                found = True
                break
        if not found:
            print(f"This {borrow_book} book is not available in the library")
    elif select == "3":
        return_book = input("Enter the name of the book you want to return: ")
        for book in books:
            if book["title"] == return_book:
                book["available"] = True
                print(f"You have returned {return_book} successfully")
                break
        else:  # If the book wasn't found
            print(f"You have not borrowed {return_book} yet")
    elif select == "5":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")