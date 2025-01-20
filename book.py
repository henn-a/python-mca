# Base class Publisher
class Publisher:
    def __init__(self, name):
        self.name = name  # Publisher's name

    def display_publisher_info(self):
        print(f"Publisher: {self.name}")


# Derived class Book from Publisher
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)  # Calling the constructor of Publisher class
        self.title = title
        self.author = author

    def display_book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


# Derived class Python from Book
class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)  # Calling the constructor of Book class
        self.price = price
        self.no_of_pages = no_of_pages

    # Method overriding to display additional information
    def display_info(self):
        self.display_publisher_info()  # Calling method from Publisher
        self.display_book_info()  # Calling method from Book
        print(f"Price: ${self.price}")
        print(f"Number of Pages: {self.no_of_pages}")


# Create an instance of the Python book
python_book = Python("O'Reilly Media", "Learning Python", "Mark Lutz", 45.99, 1500)

# Display the information about the Python book
python_book.display_info()
