from collections import Counter

word_count = Counter(input("Enter a line of text: ").split())
print(*[f"{word}: {count}" for word, count in word_count.items()], sep='\n')
