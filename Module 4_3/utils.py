import re


def get_reg_data():
    pattern_list = []

    user_name_pattern = re.compile(r'^[a-zA-Zа-яА-ЯёЁ]+$')
    pattern_list.append(user_name_pattern)

    user_last_name_pattern = re.compile(r'^[a-zA-Zа-яА-ЯёЁ]+$')
    pattern_list.append(user_last_name_pattern)

    phone_number_pattern = re.compile(r'\+\d{1,3}\(\d{2}\)\d{7}$')
    pattern_list.append(phone_number_pattern)

    mail_pattern = re.compile(r'^[a-zA-Z0-9_]+@yandex\.ru$')
    pattern_list.append(mail_pattern)

    return pattern_list

def reg_check(user_data, reg_pattern, users_list, data_to_check=None):
    while True:
        if reg_pattern.match(user_data):
            if len(users_list) > 0 and data_to_check:
                if not check_unique_data(user_data, data_to_check):
                    user_data = input()
                    continue
        else:
            print("Содержит неподходящие символы! Введите заново!")
            user_data = input()
            continue
        print("Данные приняты!")
        return user_data

def check_unique_data(user_data, data_to_check):
    if user_data in data_to_check:
        print("Такие данные уже зарегистрированны! Введите заного!")
        return False
    else:
        return True





