# Tuple
# book = ("Atomic Habits", "James Clear", "PT Gramedia Pustaka Utama", 2019)

# print(f"Title: {book[0]}")
# print(f"Writer: {book[1]}")
# print(f"Publisher: {book[2]}")
# print(f"Publication Year: {book[3]}")

# List of Tuples
books = [
    ("Atomic Habits", "James Clear", 2019),
    ("Deep Work", "Cal Newport", 2016),
    ("Clean Code", "Robert C. Martin", 2008)
]

for i, book in enumerate(books, start = 1):
    print(f"{i}. {book[0]} - {book[1]} ({book[2]})")