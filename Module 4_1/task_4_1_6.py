num = int(input("Введите число: "))

def count(num):
    a = ''
    for i in str(num):
        if i.isnumeric():
            a = a + i
    return len(a)
length = count(num)
print(f"Длина числа - {length}")