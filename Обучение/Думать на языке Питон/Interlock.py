'''Находит интерлоки. Интерлок - слово "при" и слово "вет" образуют "привет".'''
file = open('C:\word.txt')

lis = []
for el in file:
    lis.append(el.replace('\n', ''))
print(len(lis))
lis = lis[::200]
print(len(lis))


result = ''
def interlock(kraken, words, word1_kra, word2_kra):
    '''Проверяет, можно ли из букв одного слова собрать другое.'''
    krak = list(kraken)
    wo = list(words)

    krak.sort()
    wo.sort()

    global result

    if krak == wo:
        result += words + '=' + word1_kra + '+' + word2_kra + '\n'
    else:
        pass




def search(kraken, word1_kra, word2_kra):
    '''Принимает слово и находит в списке слова аналогичной длины.'''
    for words in lis:
        if len(kraken) == len(words):
            interlock(kraken, words, word1_kra, word2_kra)


def plus(word):
    for word2 in lis:
        kraken = word + word2
        search(kraken, word, word2)


for word in lis:
    plus(word)

print(result)

