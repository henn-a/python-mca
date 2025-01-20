# Lambda function to calculate area of a square
area_of_square = lambda side: side ** 2

# Lambda function to calculate area of a rectangle
area_of_rectangle = lambda length, width: length * width

# Lambda function to calculate area of a triangle
area_of_triangle = lambda base, height: 0.5 * base * height

# Example usage:

# Area of a square with side 4
square_area = area_of_square(4)
print(f"Area of square: {square_area}")

# Area of a rectangle with length 5 and width 3
rectangle_area = area_of_rectangle(5, 3)
print(f"Area of rectangle: {rectangle_area}")

# Area of a triangle with base 6 and height 4
triangle_area = area_of_triangle(6, 4)
print(f"Area of triangle: {triangle_area}")
