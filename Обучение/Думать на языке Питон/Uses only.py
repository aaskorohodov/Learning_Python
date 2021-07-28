file = open('C:\word.txt')

all_words = ''
for eo in file:
    all_words += eo
all_words = all_words.replace('\n', ' ')
'''Превращает открытый файл в строку из слов через пробел. Получается строка из множества слов.'''


def words_transmitter(all_words, letters):
    '''Принимает слова строкой и список стоп-букв.
    Создает пустой список, куда будут занесены слова без стоп-букв.
    Перебирает каждое слово, предварительно превратив строку в список из слов, разделив слова по пробелам.
    Отдает каждое слово и все стоп-буквы другой функции. Другая функция принимает решение, нужно ли включать слово в результат.'''
    result = []
    for ew in all_words.split():
        if uses_only(ew, letters) == True:
            result.append(ew)
    print(result)


def uses_only (word, letters):
    '''Принимает слово из предыдушей функции и строку стоп-букв.
    Перебирает буквы в слове, если любая буква совпадает со стоп буквой, то возвращает False
    В ином случае возвращает True, тем самым пропуская слово для записи в финальный список.'''
    for el in word:
        if el not in letters:
            return False
    return True


words_transmitter(all_words, 'acefhlo')