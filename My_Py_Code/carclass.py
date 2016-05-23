__author__ = 'sashko'


class CarClass:
    def __init__(self, brand, model, engine, price, for_sale):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.price = price
        self.for_sale = for_sale

    def print_info(self):
        print('Производитель:', self.brand)
        print('Модель:       ', self.model)
        print('Тип двигателя:', self.engine)
        print('Цена:          ', self.price, '$', sep='')
        print()

    def sale(self):
        arr = []
        if self.for_sale == 'Yes':
            arr.append(self.brand)
            arr.append(self.model)
            new_arr = " ".join(arr)
            print(new_arr)

item1 = CarClass('Audi', 'A4', 'Petrol', 35000, 'Yes')
item2 = CarClass('BMW', '320', 'Diesel', 32500, 'No')
item3 = CarClass('Chevrolet', 'Cruze', 'Petrol', 20000, 'Yes')
item4 = CarClass('Ford', 'Focus', 'Petrol', 24500, 'Yes')

all_items = [item1, item2, item3, item4]

while True:
    print('Меню:')
    print('1. Отобразить все автомобили')
    print('2. Автомобили для продажи')
    print('3. Добавить новый автомобиль')
    print('4. Выйти')
    response = input('Выберите пункт: ')
    print()

    if response == '1':
        for i in all_items:
            i.print_info()

    elif response == '2':
        for i in all_items:
            i.sale()
        print()

    elif response == '3':
        item = 'item' + (str((len(all_items)) + 1))
        input_brand = input('Введите название производителя: ')
        input_model = input('Введите название модели: ')
        input_engine = input('Введите тип двигателя: ')
        input_price = int(input('Введите цену: '))
        input_for_sale = input('Для продажи? ')
        item = CarClass(input_brand, input_model, input_engine, input_price, input_for_sale)
        all_items.append(item)
        print()

    elif response == '4':
        break

    else:
        print('Неверный ввод.')
        print()






























