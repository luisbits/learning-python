# -*- coding: utf-8 -*-
"""
1.- Ask for the number limit
2.- Let the user find de number
"""

import random


def main():
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(raw_input("Intenta un número: \n"))

        if number == random_number:
            print("Felicidades. Encontraste el número")
            number_found = True
        elif number > random_number:
            print('En número es más pequeño')
        else:
            print('El número es más grande')

if __name__ == '__main__':
    print('==== GUESS NUMBERS ====')
    main()
