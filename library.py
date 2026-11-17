
# LIBRARY MANAGEMENT SYSTEM

class Library1:

    def __init__(self):
        self.books = {
            101: ["Python Programming", "Ananya", 3],
            102: ["Java Programming", "Rahul", 2],
            103: ["Data Structures", "Priya", 4]
        }

        self.issued_books = []

    # Add Book
    def add_book(self):

        book_id = int(input("Enter Book ID: "))
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        quantity = int(input("Enter Quantity: "))

        if book_id in self.books:
            print("Book ID already exists!")

        elif quantity <= 0:
            print("Quantity must be positive!")

        else:
            self.books[book_id] = [book_name, author, quantity]
            print("Book added successfully!")

    # Display Books
    def display_books(self):

        print("\n---------- AVAILABLE BOOKS ----------")

        if not self.books:
            print("No books available.")
            return

        for book_id, details in self.books.items():

            print("\nBook ID:", book_id)
            print("Book Name:", details[0])
            print("Author:", details[1])
            print("Quantity:", details[2])

    # Search Book
    def search_book(self):

        name = input("Enter book name to search: ").lower()

        found = False

        for book_id, details in self.books.items():

            if name in details[0].lower():

                print("\nBook Found!")
                print("Book ID:", book_id)
                print("Name:", details[0])
                print("Author:", details[1])
                print("Quantity:", details[2])

                found = True

        if not found:
            print("Book not found!")

    # Issue Book
    def issue_book(self):

        book_id = int(input("Enter Book ID to issue: "))

        if book_id not in self.books:
            print("Book does not exist!")

        elif self.books[book_id][2] <= 0:
            print("Book is currently unavailable!")

        else:
            student = input("Enter Student Name: ")

            self.books[book_id][2] -= 1

            self.issued_books.append(
                (book_id, self.books[book_id][0], student)
            )

            print("Book issued successfully!")

    # Return Book
    def return_book(self):

        book_id = int(input("Enter Book ID to return: "))
        student = input("Enter Student Name: ")

        for record in self.issued_books:

            if record[0] == book_id and record[2].lower() == student.lower():

                self.issued_books.remove(record)
                self.books[book_id][2] += 1

                print("Book returned successfully!")
                return

        print("No matching issued book found!")

    # Display Issued Books
    def display_issued(self):

        print("\n---------- ISSUED BOOKS ----------")

        if not self.issued_books:
            print("No books issued.")
            return

        for book in self.issued_books:

            print("Book ID:", book[0])
            print("Book Name:", book[1])
            print("Student Name:", book[2])
            print("----------------------")

    # Delete Book
    def delete_book(self):

        book_id = int(input("Enter Book ID to delete: "))

        if book_id in self.books:

            if any(book[0] == book_id for book in self.issued_books):
                print("Cannot delete: book is currently issued!")

            else:
                del self.books[book_id]
                print("Book deleted successfully!")

        else:
            print("Book not found!")


# Main Program

library = Library()

while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Display Issued Books")
    print("7. Delete Book")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    try:

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.issue_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.display_issued()

        elif choice == "7":
            library.delete_book()

        elif choice == "8":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please try again.")

    except ValueError:
        print("Invalid input! Please enter the correct value.")
