
class Car:
    def __init__(self, company, price, color):
        self.company = company
        self.price = price
        self.color = color

   
    def display_details(self):
        print(f"Company: {self.company}")
        print(f"Price: {self.price}")
        print(f"Color: {self.color}")
       

car1 = Car("Toyota", 25000, "Red")
car2 = Car("Honda", 22000, "Blue")
car3 = Car("Ford", 28000, "Black")


print("Details of the Cars:")

car1.display_details()
car2.display_details()
car3.display_details()
