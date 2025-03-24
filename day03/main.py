import random

# a random number from 1 to 100
secret_number = random.randint(1, 100)

# a while loop that runs until the user guesses the secret number
while True:
    guess = int(input('Guess the secret number'))
    if guess == secret_number:
        print(f'You guessed the secret number! That is {secret_number}, congratulations!')
        break
    elif guess < secret_number:
        print('Try a higher number')
    else:
        print('Try a lower number')
