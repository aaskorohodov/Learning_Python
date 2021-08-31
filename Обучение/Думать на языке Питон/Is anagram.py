a = 'listen'
b = 'silent'

def is_anagram(word1, word2):
    '''Проводит 3 проверки:
    1. Совпадает ли длина слов
    2. Содержит ли первое слово все буквы второго
    3. Содержит ли второе слово все буквы первого'''
    if len(word1) != len(word2):
        return False
    for letter in word1:
        if letter not in word2:
            return False
    for letter in word2:
        if letter not in word1:
            return False
    return True

print(is_anagram(a, b))