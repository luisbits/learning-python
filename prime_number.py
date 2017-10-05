# -*- coding: utf-8 -*-
# Aprende python en http://bit.ly/luisbits-platzi

# ¿Cómo funciona?
'''
Un número primo solo es divisible entre si mismo y 1, es decir solo 2 veces.
La idea es dividir entre cada valor dentro del rango del numero ingresado.
Ejemplo: Si ingresa 7, dividir entre 1,2,3,4,5,6,7
1- Creamos una lista del número ingresado
2- Obtenemos el residuo del numero principal entre sus valores dentro del rango
3- Usando una variable como flag, si esta es mayor que 2 quiere decir que no
es un número primo. Este flag aumenta +1 cuando el residuo es = 0
'''


def main():
    print('It\'s a prime number?')
    number = int(raw_input('Type your number: \n '))
    prime_number_calculator(number)


def prime_number_calculator(number):
    flag = 0
    numbers_list = list(range(number))
    # Reading numbers list
    for n in numbers_list:
        if n > 0:
            result = number % n
            if result > 0:
                flag += 1
    # Validating if it's a prime number
    if flag > 2:
        print('{} isn\'t a prime number :('.format(number))
    else:
        print('{} is a prime number :D'.format(number))


if __name__ == '__main__':
    main()
