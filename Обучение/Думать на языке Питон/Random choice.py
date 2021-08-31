'''Выводит рандомную букву из строки. При этом вероятность вывода буквы = частоте, с которой буквы встречается в строке.'''


import random


string = 'Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo my name is A'


frequency = {}


def histogram(string):
    '''
    Делает словарь, в котором в ключе буква, а в значении частота встречи этой буквы в строке.
    '''
    for el in string.lower():
        if el not in frequency:
            frequency[el] = 1
        else:
            frequency[el] = frequency[el] + 1


frequency_clear = {}
t = []


def random_choice():
    '''
    Убирает из словаря поссчитанные пробелы, затем добавляет кажду букву в пустой список столько раз, сколько буква
    встречается в строке (какое значение в словаре для этой буквы). Затем рандомно берет букву из списка и выводит.
    '''
    histogram(string)
    for keys in frequency:
        if keys != ' ':
            frequency_clear[keys] = frequency[keys]

    for key, val in frequency_clear.items():
        for i in range(val):
            t.append(key)



random_choice()
print(random.choice(t))