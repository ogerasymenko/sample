name = None

# бесконечный цикл
while True:
    print('Меню:')
    print('1. Ввести имя')
    print('2. Вывести приветствие')
    print('3. Выйти')
    response = input('Выберите пункт: ')

    print()

    if response == '1':
        name = input('Введите ваше имя: ')
    elif response == '2':
        if name:
            print('Привет, ', name, '!', sep='')
        else:
            print('Я не знаю вашего имени.')
    elif response == '3':
            break
    else:
        print('Неверный ввод.')

    print()