alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_order = dict(zip(alphabet, range(1, 27)))

file = open('C:\word.txt')

all_words = ''
for eo in file:
    all_words += eo
all_words = all_words.replace('\n', ' ')


def order_checker(new_word):
    new_word = list(new_word.split())
    n = 0
    for en in new_word:
        try:
            if int(new_word[n]) > int(new_word[n+1]):
                return False
            else:
                n = n + 1
        except IndexError:
            return True
    return True


def order_checker2(new_word):
    new_word = list(new_word.split())
    n = 0
    for en in new_word:
        try:
            if int(new_word[n]) != (int(new_word[n+1])) - 1:
                return False
            else:
                n = n + 1
        except IndexError:
            return True
    return True


def word_to_number(word):
    new_word = ''
    for el in word:
        el = alphabet_order.get(el)
        new_word += str(el) + ' '
    return order_checker(new_word)


def word_to_number2(word):
    new_word = ''
    for el in word:
        el = alphabet_order.get(el)
        new_word += str(el) + ' '
    return order_checker2(new_word)


def all_word(all_words):
    result = []
    result2 = []

    for ew in all_words.split():
        if word_to_number(ew) == True:
            result.append(ew)

    for ew in all_words.split():
        if word_to_number2(ew) == True:
            result2.append(ew)

    print(f'Вот список слов, в которых буквы идут в алфавитном порядке:\n'
          f'{result}\n\n'
          f'Всего таких слов {len(result)} (в заданном списке слов).\n\n'
          f'Если искать только слова, сформированные прямым алфавитным порядком, то вот:\n'
          f'{result2}\n\n'
          f'Таких слов всего {len(result2)}.')


all_word(all_words)

#word_to_number(word)