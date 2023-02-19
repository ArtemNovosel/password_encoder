
def zapisat(t: str):  # функция которая будет записывать пароли/коды в файл
    if t[:15] != 'Вы использовали':  # если пароль/код валидный то записываем
        with open("myCod.txt", 'a', encoding='utf8') as a:
            a.write(f'{t}\n')


def valid_password(password):  # проверка валидности введенных символов
    with open('valid_list.txt', 'r', encoding='utf8') as valid_list:  # открываем файл с невалидными символами
        valid = valid_list.read()  # читаем его
        a = [i for i in password if i in valid]  # сверяем введенные пароль посимвольно
        if a:
            return f'Вы использовали запрещенные символы:{a}'
        elif not password:
            return 'Повторите ввод'
        else:
            zapisat(f'*{password}*')  # записываем пароль если надо
            return password  # возвращаем пароль


def koder(pasvord):  # функция кодировки
    b = []  # список кодированных символов
    a = 0  # счетчик цифр в числе
    c = 0  # счетчик чисел
    for i in pasvord + " ":  # добавляем пробел в конец, для корректной обработки цифры в конце пароля
        if i.isdigit():  # если символ -цифра
            c = c * 10 + int(i)  # запускаем счетчик числа
            a += 1  # увеличиваем счетчик цифр
        elif a != 0:  # если цифры есть
            b.append(str(c + 100))  # увеличиваем число на 100, вносим в список
            a = 0  # обнуляем счетчик
            b.append(i)  # добавляем символ
        else:
            b.append(i)
    zapisat(''.join(b[0:-1]))  # записываем кодированный пароль в файл
    return ''.join(b[0:-1])


print(koder(valid_password(input('Введите пароль: '))), end=' ')