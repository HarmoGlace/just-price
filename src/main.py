from os import system, name
from termcolor import colored
from party import Party


def clear_console():
    return system('cls' if name == 'nt' else 'clear')


party = Party()

while not party.finished:
    min, max = party.given_near
    print(f'min: {min}      max: {max}')
    try:
        given = int(input('Give me a number: '))
        if given > party.max or given < party.min: raise ValueError('range')
    except ValueError:
        clear_console()
        print(colored(f'Please give a valid number between {party.min} and {party.max}.', 'red'))
        continue

    party.tries.add(given)

    print(f'It is {"more" if given < party.result else "less"} than {given}')
    clear_console()

print(f'Indeed it was {party.result}, gg !')