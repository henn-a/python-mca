colors = input("Enter colors : ").split(',')

print("First color:", colors[0].strip() if colors else "None")
print("Last color:", colors[-1].strip() if colors else "None")
