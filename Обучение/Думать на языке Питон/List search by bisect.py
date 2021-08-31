import bisect
'''Выполняет поиск елемента в отсортированном списке. Именно в отсортированном.'''

file = open('C:\word.txt')
lis = []
for el in file:
    el = el.replace('\n', '')
    lis.append(el)
'''Открывает файл и превращает его в список, убрав переносы строки (в файле много слов, каждое слово с новой строки).'''


def search(lis, word):
    '''Принимает список и слово, которое надо найти.
    1. Переменная index показывает место в списке, справа от искомого слова (т.е. +1). Так происходит, потому что
    bisect ищет место, в которое заданное слово надо поставить, чтобы сохранить отсортированность списка.
    Он принимает слово, например hello, ищет место, куда его поставить, и место получается правее другого слова hello,
    которе уже есть в списке. Т.е. он находи слово hello и предлагает поставить другое слово hello правее на 1.
    2. if получает индекс (куда поставить слово), и проверяет, чтобы на предыдущем месте было искомое слово.
    3. Если слово на месте, то отдается текст, мол "нашлось ваше слово, оно тут..."
    4. Если слова нет (по индексу стоит другое слово, а не переданное в фунцию), то выдает другой текст.
    Почему там другое слово – потому что bisect просто находит место, куда можно поставить переданное ему слово,
    его не интересует, содержится ли это слово в списке, он просто ищет подходящее место.
    Так что может так получится, что bisect нашел место для заданного слова hello, которое будет сразу после hell.'''
    index = bisect.bisect(lis, word)
    if lis[index - 1] == word:
        return f'Слово {word} находится в списке по идкесу {index - 1}\n' \
               f'Убедитесь сами, вызвав елемент с таким индексом:\n' \
               f'print(lis[{index - 1}])'
    else:
        return f'Слово {word} отсутствует в списке'


print(search(lis, 'hello'))