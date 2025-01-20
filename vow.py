string=input("enter the string:")
print("Vowels in given string are:")
for letter in string:
    if letter in 'aeiou':
        print(letter,end=" ")
