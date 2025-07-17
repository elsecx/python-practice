# Tuple
book = ("Atomic Habits", "James Clear", 2019)

print(f"Title: {book[0]}")
print(f"Writer: {book[1]}")
print(f"Publication Year: {book[2]}\n")

# use unpacking
title, writer, year = book
print(f"{title} - {writer} ({year})\n")

# List of Tuples
books = [
    ("Atomic Habits", "James Clear", 2019),
    ("Deep Work", "Cal Newport", 2016),
    ("Clean Code", "Robert C. Martin", 2008)
]

for i, book in enumerate(books, start = 1):
    print(f"{i}. {book[0]} - {book[1]} ({book[2]})")
print("\n")

# Set
a = {1, 2, 3}
b = {3, 4, 5}

print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference (a - b): {a - b}")