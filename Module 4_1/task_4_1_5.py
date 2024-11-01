start = int(input("Введите начало диапозона: "))
end = int(input("Введите конец диапозона: "))

def multiplication(start, end):
    if start > end:
        start, end = end, start
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result
x = multiplication(start, end)
print(f"Произведение чисел в диапозоне равно {x}")