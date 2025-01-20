class Publisher:
    def __init__(self, name):
        self.name = name

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def show_Details(self):
        print(f"Publisher : {self.name}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")

class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)  # Base class constructor invocation
        self.price = price
        self.no_of_pages = no_of_pages

    def show_Details(self):  # Method Overriding
        print(f"Publisher : {self.name}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Price : {self.price}")
        print(f"Pages : {self.no_of_pages}")

# Create an instance of the Python class
b1 = Python("SHAMIL", "We Live In A Time", "Peter", "Rs.1050", 173)
b1.show_Details()
