num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
num4 = int(input("Введите четвёртое число: "))
num5 = int(input("Введите пятое число: "))

def num(num1, num2, num3, num4, num5):
    return min(num1, num2, num3, num4, num5)
min_num = num(num1, num2, num3, num4, num5)
print(min_num)