'''
program to guess a random number
'''

__author__ = 'sashko'

# import random module to generate random number
import random

# generate random number
secret_number = random.randint(1, 101)

# count of attempts
num_of_attempts = 1

# input first number
attempt = int(input('Input a number in range 1 - 100: '))

# in while loop we compare inputted number with random number
while attempt != secret_number:
    if attempt > secret_number:
        print('Number is less than', attempt)
    else:
        print('Number is grater than', attempt)

    # increase num_of_attempts after each attempt
    num_of_attempts += 1
    attempt = int(input('Input a number: '))

# after guessing correct number print this number
print('Right number is', secret_number)
# and quantity of attempts
print('You guess it in', num_of_attempts, 'attempts')
