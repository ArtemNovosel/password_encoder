import re
password_list = []
password = input('Введите пароль: ')  # получаем пароль от пользователя
# print(len(password))

chisla = re.findall(r'\d*\d+|\d+', password)
chisla = [int(i) for i in chisla]  # вычленяем из пароля числа
# print(chisla)

valid_list = ['/', ',', '.', ' ', "'", '-', '"']  # вносим символы в список исключений
a = [i for i in password if i in valid_list]  # колличество невалидных символов в password
# print(a)
if a:
    print('Вы использовали запрещенные символы: ', *a)

# /дальше блок преобразования
else:
    b = -1
    c = 0
    for i in password:
        if i.isdigit():  # натыкаясь на цифру добавляем в список число
            while c < 1:
                b = b + 1  # которое соответствует колличеству проходов b
                password_list.append(chisla[b] + 100)
                c = 1  # игнорим остальные цифры в числе
        else:
            c = 0  # включаем условие для блока цифр
            password_list.append(i)
    # print(password_list)
    kod_password = str(password_list).replace(", ", "")
    kod_password = kod_password[1:-1].replace("'", "")
    print(kod_password)
# else:
#     print("Вы использовали запрещенные символы")