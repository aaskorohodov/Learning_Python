import string


def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)

    return hist


def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


hist = process_file(r'C:\Users\Аркадий\Downloads\emma.txt')

hist = set(hist)

file = open('C:\word.txt')


words = ''
for el in file:
    words += el


words_clean = []
for el in words.split('\n'):
    words_clean.append(el)


words_clean = set(words_clean)

print(words_clean)
#print(hist.difference(words_clean))