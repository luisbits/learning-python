# -*- coding: utf-8 -*-
# Aprende python en http://bit.ly/luisbits-platzi

import turtle


def main():
    # window = turtle.Screen()
    dave = turtle.Turtle()
    make_square(dave)


def make_square(dave):
    raw_input()
    length = int(raw_input('Tamaño de cuadrado: '))
    for i in range(4):
        make_line_and_turn(dave, length)
        pass
    raw_input('Presiona enter/intro para finalizar :D')


def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)


if __name__ == '__main__':
    main()
