# -*- coding: utf-8 -*-
"""
1.- Ask for number of temperatures
2.- Ask for each temperature
3.- Show the result
"""


def avarage_temps(options):
    temps = []
    sum_of_temps = 0

    for option in options:
        temperature = int(raw_input('Ingrese temperatura: '))
        temps.insert(0, temperature)

    for temp in temps:
        sum_of_temps += float(temp)

    return sum_of_temps / len(temps)

if __name__ == '__main__':
    options = int(raw_input('Temperaturas a calcular (ingrese numero): '))

    avarage = avarage_temps(options)
    print('La temperatura promedio es: {}'.format(avarage))
