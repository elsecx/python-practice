print("Operator yang dapat dimasukkan adalah sebagai berikut: (+, -, *, /)")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
operator = input("Masukkan operator: ")

def calculator(a, b, operator):
    if operator == "/" and b == 0:
        return "Tidak bisa membagi dengan nol"

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Operator tidak valid!"

print(calculator(a, b, operator))