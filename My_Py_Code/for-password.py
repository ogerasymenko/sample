for attempts_left in range (4, 1, -1):
	attempts_left -=1
	password = input('Enter your password. You have {} attempts left: '.format(attempts_left))
	if password == 'passwd':
		print('Access allowed')
		break
else:
	print('Access denied')
