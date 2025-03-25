import random

print('Welcome to PyPassword Generator!')
num_letter = int(input('How many letters would you like in your password?\n'))
num_symbol = int(input('How many symbols would you like?\n'))
num_number = int(input('How many numbers would you like?\n'))

letter = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(num_letter)]
symbol = [random.choice('!@#$%^&*()_+') for _ in range(num_symbol)]
number = [random.choice('0123456789') for _ in range(num_number)]
password = letter + symbol + number

random.shuffle(password)
print(f'yout password is: {"".join(password)}')
