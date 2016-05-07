x = float(input('Сумма: '))
y = x * 0.2
z = x - y
print('Сумма с вычетом налогов составляет:', int(z), 'грн')
usdcalc = input('Вы хотите пересчитать сумму в долларах США? ')
if usdcalc == 'yes':
        curs = float(input('Введите текущий курс доллара: '))
        usdsum = z/curs
        print('Сумма в доларах США составляет:', int(usdsum), '$')
elif usdcalc == 'no':
    print('Удачи!')
elif usdcalc != 'yes':
        while usdcalc != 'yes':
            usdcalc = input('Введите yes или no: ')
            if usdcalc == 'yes':
                curs = float(input('Введите текущий курс доллара: '))
                usdsum = z/curs
                print('Сумма в доларах США составляет:', int(usdsum), '$')
                break
            elif usdcalc == 'no':
                print('Удачи!')
                break











