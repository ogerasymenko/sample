# Функция, которая принимает три аргумента

def info(object, color, price):
    print()
    print('Объект:', object)
    print('Цвет:', color)
    print('Цена: ', price, '$', sep='')

# передача параметров в прямом порядке
# info('pen', 'blue', 7)
# передача параметров в произвольном порядке
# info(price=5, object='cup', color='orange')
# можно смешивать оба способа, но сначала должны идти параметры,
# которые передаются в прямом порядке
# info('cofee', price=99, color='black')

obj = input('Введите название объекта: ')
col = input('Введите цвет: ')
cena = input('Введите цену: ')

info(obj, col, cena)
