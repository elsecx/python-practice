# Create list of number from 0 to 9
numbers = [i for i in range(10)]
print(numbers)

# With Condition (filter)
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# With Expression
squares = [i**2 for i in range(5)]
print(squares)

# Practice
# 1
words = ["learn", "python", "with", "focus", "and", "consistency"]
uppercase = [w.upper() for w in words]
print(uppercase)

# 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

multiples_of_3 = [n for n in numbers if n % 3 == 0]
print(multiples_of_3)

# 3
# def condition(n):
#     if n % 2:
#         return "ganjil"
#     else:
#         return "genap"
# odd_even = [condition(n) for n in numbers]
# print(odd_even)
odd_even = ["ganjil" if n % 2 else "genap" for n in numbers]
print(odd_even)