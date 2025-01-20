from datetime import datetime

f = int(input("Enter final year: "))
cy = datetime.now().year
print("The leap years are:")
print([y for y in range(cy + 1, f + 1) if f > cy and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))]
      or "Must be greater than current year.")
