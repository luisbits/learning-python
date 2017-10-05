# -*- coding: utf-8 -*-
# Aprende python en http://bit.ly/luisbits-platzi


def exchange_calculator(ammount):
    mxn_to_cop = 145.97
    return mxn_to_cop * ammount


def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos mexicanos a pesos colombianos.')
    print('')

    ammount = float(raw_input('Ingrese cantidad en MXN a convertir: \n'))
    result = exchange_calculator(ammount)
    print('${} MXN son ${} COP'.format(ammount, result))


if __name__ == '__main__':
    run()
