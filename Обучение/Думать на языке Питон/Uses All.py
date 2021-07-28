file = open('C:\word.txt')

all_words = ''
for eo in file:
    all_words += eo
all_words = all_words.replace('\n', ' ')
'''Создает строку, в которой содержатся все слова из файла через пробел.'''

def uses_all(word, letters):
    '''Принимает слово и строку букв. Проверяет каждую букву в слове, если каждая буква в слове есть в строке букв, то возвращает True.'''
    for letter in word:
        if letter not in letters:
            return False
    return True


def asd(all_words, letters):
    '''Принимает строку слов и строку букв. Превращает строку слов в список слов, перебирает каждое слово, отдавая его в другую функцию вместе со списком букв.
    Если другая функция отдает Тру (все буквы в слове есть и в списке букв), то записывает слово в результат.'''
    result = []
    for ew in all_words.split():
        if uses_all(ew, letters) == True:
            result.append(ew)
    print(result)
    print(len(result))

asd(all_words, 'aeiouy')