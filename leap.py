final_year = int(input("Enter the final year: "))
print("Future Leap Years:")
for year in range(current_year + 1, final_year + 1):
     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year)
