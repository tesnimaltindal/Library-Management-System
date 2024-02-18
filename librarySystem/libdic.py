
#Tesnim ALTINDAL
#library management system


class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.books = []  # List to store books

        # Load existing books from file
        self.load_books()
    
    # Destructor method.
    # Called when the object is about to be destroyed.Close the file.
    def __del__(self):
        self.file.close()
        

    def load_books(self):
       
            with open(self.file_path, "a+") as file:
                for line in file:
                    title, author, release_year, pages = line.strip().split(',')
                    book = {
                        'title': title,
                        'author': author,
                        'release_year': int(release_year),
                        'pages': int(pages)
                    }
                    self.books.append(book)

    def save_books(self):
        with open(self.file_path, "a+") as file:
            for book in self.books:
                file.write(f"{book['title']},{book['author']},{book['release_year']},{book['pages']}\n")

    def list_books(self):
        if not self.books:
            print("No books available.")
            return

        print("List of Books:")
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, Release Year: {book['release_year']}, Pages: {book['pages']}")

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")

        while True:
            try:
                release_year = int(input("Enter the first release year: "))
                break  # Break out of the loop if conversion to int is successful
            except ValueError:
                print("Invalid input. Please enter a valid integer for the release year.")

        while True:
            try:
                pages = int(input("Enter the number of pages: "))
                break  # Break out of the loop if conversion to int is successful
            except ValueError:
                print("Invalid input. Please enter a valid integer for the number of pages.")

        book = {
            'title': title,
            'author': author,
            'release_year': release_year,
            'pages': pages
        }

        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' has been added successfully.")

    def remove_book(self):
        if not self.books:
            print("No books available. Nothing to remove.")
            return

        title_to_remove = input("Enter the title of the book to remove: ")

        found = False
        new_books_list = []

        for book in self.books:
            if title_to_remove != book['title']:
                new_books_list.append(book)
            else:
                found = True

        if not found:
            print(f"Book '{title_to_remove}' not found. Nothing to remove.")
            return

        self.books = new_books_list
        self.save_books()

        print(f"Book '{title_to_remove}' has been removed successfully.")


# Create the Library object
lib = Library()

# Menu
while True:
    print("\n*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        lib.__del__
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
