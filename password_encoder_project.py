password_list = []
password = input('Введите символы: ')  # получаем пароль от пользователя
for i in password:  # в цикле к каждое значение уваличиваем на 100
    if i.isdigit():
      password_list.append(int(i) + 100)  # записываем результат в password_list
    else:
      password_list.append('100' + i)  # записываем результат в password_list
# print(password_list)
kod_password = str(password_list).replace(", ", "")  # password_list преобразовываем в строку удалив лишние символы
kod_password = kod_password[1:-1].replace("'","")
print("Кодированный пароль: ", kod_password)