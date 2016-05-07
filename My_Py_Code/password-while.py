attempts_left = 3
while attempts_left > 0:
	attempts_left -=1
	password = input('Enter your password. You have {} attempts left: '.format(attempts_left + 1))
	if password == 'passwd':
		print('Access allowed')
		break
else:
	print('Access denied')
