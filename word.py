# Taking input from the user
sentence = input("Enter the sentence: ")
words = sentence.split()

# Create a dictionary to store word count
word_count = {}

# Count the occurrences of each word
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Output the word count
for word in word_count:
    print(f"{word}: {word_count[word]}")

# Search for a particular word
search_word = input("\nEnter the word you want to search for: ")

# Check if the word is in the sentence and display the count
if search_word in word_count:
    print(f"The word '{search_word}' appears {word_count[search_word]} time(s).")
else:
    print(f"The word '{search_word}' is not in the sentence.")
