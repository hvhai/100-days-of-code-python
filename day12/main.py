from random import randint
import re


logo = '''
 ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

'''


def select_mode():
    """
    Select the difficulty level for the game.
    """
    while True:
        diffculty = input('Choose a difficulty. Type "easy" or "hard": ')
        if diffculty == 'easy':
            return 10
        elif diffculty == 'hard':
            return 5
        else:
            print('Invalid input. Please try again.')


def guess_number(secret_number, attempts):
    while attempts > 0:
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = input('Make a guess: ')
        if not re.match(r'^[0-9]+$', guess):
            print('Please enter a valid number.')
            continue
        guess = int(guess)
        if guess == secret_number:
            print(f'You guessed the secret number! That is {secret_number}, congratulations!')
            break
        elif guess < secret_number:
            print('Try a higher number')
        else:
            print('Try a lower number')
        attempts -= 1


if __name__ == "__main__":
    print(logo)
    secret_number = randint(1, 100)
    print('A random number from 1 to 100 has been generated.\nTry to guess the secret number.')
    attempts = select_mode()
    guess_number(secret_number, attempts)
