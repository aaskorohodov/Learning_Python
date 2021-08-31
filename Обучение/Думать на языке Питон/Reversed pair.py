import bisect


file = open('C:\word.txt')


lis = []
for el in file:
    lis.append(el.replace('\n', ''))


def word_reversed(word):
    word = word[::-1]
    return word


def search(lis, word):
    index = bisect.bisect(lis, word)
    if lis[index - 1] == word:
        return index - 1
    else:
        return False


resl = []
result = ''
for word in lis:
    if search(lis, word_reversed(word)) == False:
        pass
    else:
        if search(lis, word) > search(lis, word_reversed(word)):
            pass
        else:
            i = search(lis, word_reversed(word))

            resl.append(word)
            resl.append(lis[i])

            i = search(lis, word_reversed(word))
            result += word + ' – ' + lis[i] + '\n'


print(result)