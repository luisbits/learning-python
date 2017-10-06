# -*- coding: utf-8 -*-
# Aprende python en http://bit.ly/luisbits-platzi


def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


if __name__ == '__main__':
    number = int(raw_input('Ingrese un número: \n'))
    result = factorial(number)
    print('El factorial de {} es {}'.format(number, result))
