# *args
def multiply_all(*args):
    total = 1
    for num in args:
        total *= num
    return total

print(multiply_all(2, 3, 4))

# **kwargs
# biodata = []

def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

introduce(name = "Elgin Al-wafi", age = 18, country = "Indonesia")