# Пример 1
def new_multiplication(*args):
    multiplication = 1
    for num in args:
        multiplication *= num
    return multiplication


new_multiplication_ = new_multiplication(1, 5, 8, 9)
print("Новое произведение:", new_multiplication_)


# Пример 2
def get_shortest_word(*args):
    shortest_word = args[0]  # Выберем первое слово, как свмое маленькое
    shortest_length = len(shortest_word)
    for word in args:
        if shortest_length > len(word):
            shortest_length = len(word)
            shortest_word = word
    return shortest_word


shortest_word_ = get_shortest_word("Москва", "Уфа", "Сочи", "Липецк")
print("Самое короткое слово:", shortest_word_)


# Пример 3
def get_string(string, *args):
    for symbol in args:
        string = string.replace(symbol, ", ")
    return string


print(get_string("Соль сахар перец", " "))

print()


# Пример 4
def info_about_album(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


info_about_album(Album="Rude the lightning", Band="Metallica", Genre="Thrash Metal", Release="1985")

print()


# Пример 5
def info_about_movie(*args, **kwargs):
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(key, ":", value)


info_about_movie("Batman", "Movie Comics", Director="Tim Burton", Release="1989")
