def input_number():
    loop = True
    while loop:
        try:
            number = float(input('Введите сумму: '))
            return number
            loop = False
        except (ValueError):
            print('Введите сумму числом!')
            loop = True

x = input_number()
y = x * 0.2
z = x - y
print('Сумма с учетом налогов составляет:', int(z), 'грн')

def usd_func():
    loop = True
    while loop:
        try:
            curs = float(input('Введите текущий курс доллара: '))
            usd = z/curs
            return usd
            loop = False
        except (ValueError):
            print('Введите курс числом!')
            loop = True


def result():
    usdsum = usd_func() 
    print('Сумма в доларах США составляет:', int(usdsum), '$')

usdcalc = input('Вы хотите пересчитать сумму в долларах США? ')

if usdcalc == 'yes':
    result()

elif usdcalc == 'no':
    print('Удачи!')

elif usdcalc != 'yes':
        while usdcalc != 'yes':
            usdcalc = input('Введите yes или no: ')
            if usdcalc == 'yes':
                result()
                break
            elif usdcalc == 'no':
                print('Удачи!')
                break
