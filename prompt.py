def get_integers_above_100():
    numbers = map(int, input("Enter integers separated by spaces: ").split())
    above_100 = [num for num in numbers if num > 100]
    return above_100

result = get_integers_above_100()
print("Integers greater than 100:", result)
