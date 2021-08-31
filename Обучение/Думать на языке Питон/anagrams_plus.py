'''Ищет в списке слов анаграмы и собирает их в кучки "из этих букв можно сделать эти слова"'''

file = open('C:\word.txt')

words = ''
for eo in file:
    words += eo


def letters(word):
    '''
    Вспомогательная функция, берет слово и сортирует буквы по алфавиту.
    Из интересного join – собирает список в строку. Ставится поверх строки, тут это пустая строка ''. Если сотавить
    в строке какой-то символ, то в результате этот символ будет стоять через каждый элемент списка.
    '''
    let = list(word)
    let.sort()
    let = ''.join(let)

    return let


def anagrams(all_words):
    '''
    Основная функция – ищет анаграмы и собирает из в словарь, где ключ = буквы, значение = слова из этих букв.
    1. Делаем пустой словарь
    2. Перебираем элементы (слова) в строке слов. Там слова с новой строки, так что делим изходную строку через \n
    3. В переборе создаем временную l, туда кладем буквы, из которых состоит каждое слово
    4. Если l нет в пустом словаре, то записываем его в ключ, а значением ставим слово, из которого эти буквы родились.
    *значение ставим в список [], потому что из этих букв могут быть и другие слова, которые можно будет положить
    в этот же список с помощью append.
    5. А если l есть в словаре, то по ключу l (в значение) кладет это слово (в список).
    '''
    an_dict = {}
    for el in all_words.split('\n'):
        l = letters(el)

        if l not in an_dict:
            an_dict[l] = [el]
        else:
            an_dict[l].append(el)

    return an_dict


def print_anagrams_in_num(words, num):
    '''Печатает все анаграммы, которых больше чем мы захотим. Пр: покажи все анаграммы, которых получается больше чем х'''
    an_dict = anagrams(words)

    for el in an_dict.values():
        if len(el) > num:
            print(el)


def print_anagrams_in_order(words):
    '''Печатает анаграммы в порядке их количества. Для этого в список списков заносятся сначала длина значения словаря
    (т.е. сколько там в списке слов), а потом самы слова'''
    an_list = []
    an_dict = anagrams(words)

    for el in an_dict.values():
        if len(el) > 1:
            an_list.append((len(el), el))

    an_list.sort()

    for el in an_list:
        print(el[1])


def anagrams_from_x_letters(num, length):
    '''Ищет анаграмы определенной длины (кол-во букв) и в определенном количестве (слов из этих букв). Все аналогично.'''
    an_list = []
    an_dict = anagrams(words)

    for kraken, anagram in an_dict.items():
        if len(anagram) > length:
            if len(kraken) == num:
                an_list.append((kraken, anagram))

    print(an_list)


anagrams_from_x_letters(8, 6)