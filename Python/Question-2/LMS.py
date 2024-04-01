import datetime

class LibraryManagementSystem:
    '''A class representing a Library Management System'''

    def __init__(self, list_of_books_file, library_name):
        '''Initialize the library with book data, user data, and transaction data'''
        self.list_of_books_file = list_of_books_file
        self.library_name = library_name
        self.books = {}
        self.users = {}
        self.transactions = {}
        self.load_books_data()

    def load_books_data(self):
        '''Load book data from a file'''
        with open(self.list_of_books_file) as file:
            for book_id, title in enumerate(file, 101):
                self.books[str(book_id)] = {
                    "title": title.strip(),
                    "lender_name": "",
                    "issue_date": "",
                    "status": "Available"
                }

    def display_books(self):
        '''Display the list of books along with their details'''
        print("Book ID\tTitle\tUser ID\tIssue Date\tStatus")
        print("_____________________________________________________")
        for book_id, info in self.books.items():
            user_id = self.transactions.get(book_id, [""])[0]
            issue_date = info["issue_date"]
            print(f"{book_id}\t{info['title']}\t{user_id}\t{issue_date}\t{info['status']}")

    def issue_book(self):
        '''Issue a book to a user'''
        book_id = input("Enter book ID: ")
        if book_id in self.books:
            if self.books[book_id]["status"] == "Available":
                if len(self.transactions.get(book_id, [])) < 3:
                    user_id = input("Enter user ID: ")
                    if user_id in self.users:
                        self.books[book_id]["lender_name"] = self.users[user_id]["name"]
                        self.books[book_id]["issue_date"] = datetime.datetime.now().strftime("%Y-%m-%d")
                        self.books[book_id]["status"] = "Issued"
                        self.transactions.setdefault(book_id, []).append(user_id)
                        print("Book issued successfully!")
                    else:
                        print("User not found. Please register first.")
                else:
                    print("You have already issued 3 books.")
            else:
                print("This book is already issued.")
        else:
            print("Book ID not found.")

    # Implement other methods: add_book, return_book, register_user, overdue_books, etc.

try:
    lms = LibraryManagementSystem("List_of_books.txt", "Python's Library")
    while True:
        print("\n----------------------Welcome TO", lms.library_name, "Library management System----------------\n")
        print("Press D to Display Books")
        print("Press I to Issue Books")
        print("Press A to Add Books")
        print("Press R to Return Books")
        print("Press U to User Registration")
        print("Press O to Overdue Books")
        print("Press Q to Quit")
        choice = input("Enter your choice: ").lower()
        if choice == "d":
            lms.display_books()
        elif choice == "i":
            lms.issue_book()
        # Add other menu options here
        elif choice == "q":
            break
except Exception as e:
    print("An error occurred:", e)
