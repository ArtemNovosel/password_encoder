password_list = []
try:
    password = input('Введите цифры: ')  # получаем пароль от пользователя
    # print(password)
    for i in password:  # в цикле к каждое значение уваличиваем на 100
        password_list.append(int(i) + 100)  # записываем результат в password_list
        # print(password_list)

except ValueError as e:  # ловим ошибку при введении посторонних символов
    print('Введите только цифры!')

else:
    kod_password = str(password_list)[1:-1].replace(", ", "")  # password_list преобразовываем в страку удалив лишние символы
    print("Кодированный пароль: ", kod_password)