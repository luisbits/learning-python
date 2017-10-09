# -*- coding: utf-8 -*-


def palindrome_checker(word):
    word = word.lower()
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True

    return False


def palindrome_light(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True
    return False


if __name__ == '__main__':
    print('=== ¿Es palíndromo? ===')
    word = str(raw_input('Escribe una palabra: \n'))

    result = palindrome_light(word)

    if result is True:
        print('{} es un palíndromo'.format(word))
    else:
        print('{} NO es un palíndromo'.format(word))
