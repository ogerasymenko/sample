import random

def pwd_gen(count_char=8):
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R' 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '$', '%', '&', '{', '}', '(', ')'
    '-', '+','_']
    
    password = []
    for i in range(count_char):
        password.append(random.choice(arr))
    return "".join(password)

pw_length = input('Введите длинну пароля: ')
if pw_length =='':
    print('Вы не ввели число.')

if pw_length[0:].isdigit():
	print(pwd_gen(int(pw_length)))
