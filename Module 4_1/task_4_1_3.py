length_1 = int(input("Введите длину стороны квадрата: "))
symbol_1 = input("Введите символ: ")
length_2 = int(input("Введите длину стороны квадрата: "))
symbol_2 = input("Введите символ: ")

def square(length, symbol, logic):
    for i in range(length):
        if logic or i == 0 or i == (length - 1):
            print(symbol * length)
        else:
            print(symbol + (' ' * (length - 2)) + symbol)

square(length_1, symbol_1, False)
print()
square(length_2, symbol_2, True)