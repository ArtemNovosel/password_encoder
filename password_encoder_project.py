valid_list = ['/', ',', '.', ' ', "'", '-', '"', '']  # вносим символы в список исключений
def valid_password(password):
        a = [i for i in password if i in valid_list]
        if a:
            return f'Вы использовали запрещенные символы:{a}'
        else:
            return password
def koder(fn):
    pasvord = fn
    b = []
    a = 0
    for i in pasvord+" ":
        if i.isdigit():
            a = a * 10 + int(i)
        elif a != 0:
            b.append(str(a + 100))
            a = 0
            b.append(i)
        else:
            b.append(i)
    return ''.join(b[0:-1])
print(koder(valid_password(input('Введите пароль: '))))