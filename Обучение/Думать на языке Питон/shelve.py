import shelve


def store_anagrams(filename, anagram_map):
    """Stores the anagrams from a dictionary in a shelf.
    filename: string file name of shelf
    anagram_map: dictionary that maps strings to list of anagrams
    """
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()


def signature(s):
    """Returns the signature of this string.
    Signature is a string that contains all of the letters in order.
    s: string
    """
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Finds all anagrams in a list of words.
    filename: string filename of the word list
    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    store_anagrams('C:\\Users\\Аркадий\\Тест Фолдер\\123.txt', d)


def read_anagrams(filename, word):
    """Looks up a word in a shelf and returns a list of its anagrams.
    filename: string file name of shelf
    word: word to look up
    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


print(read_anagrams('C:\\Users\\Аркадий\\Тест Фолдер\\123.txt', 'absents'))