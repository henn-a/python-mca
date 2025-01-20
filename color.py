colors = [c.strip() for c in input("Enter colors separated by commas: ").split(',')]
if colors:
    print("First color:", colors[0], "\nLast color:", colors[-1])
else:
    print("No colors entered.")
