from os import system, name
from termcolor import colored
from party import Party


def clear_console():
    return system('cls' if name == 'nt' else 'clear')


party = Party()

while not party.finished:
    try:
        given = int(input('Give me a number: '))
    except ValueError:
        clear_console()
        print(colored('Please give a valid number.', 'red'))
        continue

    party.tries.add(given)
    if given < party.result:
        print(f'It is {"more" if given < party.result else "less"} than {given}')

print(f'Indeed it was {party.result}, gg !')