import math


area_of_circle = lambda r: math.pi * r ** 2


radius = float(input("Enter the radius of the circle: "))


area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")
