import time


def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_polindrome(word, x):
    if len(word) > 2 and first(word) == last(word):
        is_polindrome(middle(word), x)
    else:
        if len(word) >= 2 and first(word) == last(word):
            print(f'\nСлово "{x}" полиндром')
            time.sleep(1)
            inp2()
        elif len(word) == 0:
            print('\nВы ввели пустую строку')
            time.sleep(1)
            inp2()
        else:
            print(f'\nСлово "{x}" не полиндром')
            time.sleep(1)
            inp2()


def inp():
    word = input('Тут можно узнать, является ли ваше слово полиндромом.\n'
                    'Введите слово: ')
    x = word
    word_length(word)

def inp2():
    word = input('\nВведите еще слово на проверку, или введите "хватит" для завершения (слово "хватит" не полиндром): ')
    x = word
    if word.lower() == 'хватит':
        print('\nДосвидания :*'
              '\n')
        time.sleep(5)
        quit()
    else:
        word_length(word)

def word_length(word):
    x = word
    if len(list(word.split())) > 1:
        word = input("\nАтата, вводите 1 слово: ")
        word_length(word)
    else:
        is_polindrome(word, x)

inp()
