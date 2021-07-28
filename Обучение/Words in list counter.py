print("Эта херотень посчитает количество уникальных слов.")
words = input("Введите слова через пробел, точку, запятую или другой удобный знак:")
print("Ваш списко слов: " + words)

words = words.lower()
words = words.replace(",", " ")
words = words.replace(":", " ")
words = words.replace(".", " ")
words = words.replace("/", " ")
words = words.replace("%", " ")
words = words.replace("|", " ")
words = words.replace("!", " ")
words = words.replace("@", " ")
words = words.replace("#", " ")
words = words.replace("$", " ")
words = words.replace("?", " ")
words = words.split()
print(words)

temp = []
e = 0
for x in words:
    if x in temp:
        pass
    else:
        temp.append(x)
        e += 1

print("Всего тут " + str(e) + " уникальных слов")