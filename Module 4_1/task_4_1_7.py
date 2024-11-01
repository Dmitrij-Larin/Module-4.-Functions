num = int(input("Введите число: "))

def palindrom(num):
    pal = str(num)
    return (pal[::-1] == pal)
x = palindrom(num)
if x == True:
    print(f"Число {num} является палиндромом")
else:
    print(f"Число {num} не является палиндромом")