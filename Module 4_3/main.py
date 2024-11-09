from utils import get_reg_data, reg_check

users_list = []
check_phone_list = []
check_email_list = []
check_unique_list = [None, None, check_phone_list, check_email_list]
types = ["имя", "фамилию", "телефон в формате +***(**)*******", "email на Яндексе"]

reg_data_list = get_reg_data()

while len(users_list) < 3:
    user_data_list = []
    counter = 0
    for i in range(4):
        user_data = input(f"Введите {types[counter]} пользователя: ")
        right_user_data = reg_check(user_data, reg_data_list[counter], users_list, check_unique_list[counter])
        if right_user_data:
            counter += 1
            user_data_list.append(right_user_data)
            pass
        else:
            continue

    users_list.append(user_data_list)
    check_phone_list.append(user_data_list[2])
    check_email_list.append(user_data_list[3])
    print()

for user_data_list in users_list:
    print(user_data_list)
