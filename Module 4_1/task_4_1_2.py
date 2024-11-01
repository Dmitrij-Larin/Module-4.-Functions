num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

def num(num1, num2):
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i)
num(num1, num2)



