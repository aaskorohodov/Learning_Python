print("Это программа посчитает количество повторяющихся слов в тексте.")
words = input("Введите ваш текст: ")

del_sym = str.maketrans({
    "!": None,
    ".": None,
    "@": None,
    "#": None,
    "$": None,
    "%": None,
    "^": None,
    "&": None,
    "*": None,
    "(": None,
    ")": None,
    "_": None,
    "-": " ",
    "=": None,
    "+": None,
    "[": None,
    "]": None,
    "|": None,
    "/": None,
    ",": None,
    "<": None,
    ">": None,
    "{": None,
    "}": None,
    "№": None,
    ";": None,
    ":": None,
    "?": None
})
words = words.translate(del_sym)
words = words.lower()
words = words.split()

dict = {}                                         #ниже создается словарь (слово:количество повторов)
for eo in words:
    if eo in dict:
        dict[eo] = dict[eo] + 1                   #часть до знака = присваевает словарю ключ со значением ео, часть справа от = повышает значение ключа ео на 1
    else:
        dict[eo] = 1                              #это создает пару ключ:значение. Создается ключ ео и ему дается значение 1.

sorted_values = sorted(dict.values())             #сортирует значения, записывает их в переменную
sorted_dict = {}

for ev in sorted_values:                          #перебираем ранее отсортированные значения
    for ek in dict.keys():                        #с каждым значением перебираем ключ
        if dict[ek] == ev:                        #если значение ключа (то есть именно значение, цифра) совпадает с отсортированной цифрой...
            sorted_dict[ek] = dict[ek]            #...то кладем этот ключ с этим значением в новый словарь.

onesexcluded_dict = {}                            #это надо, чтобы убрать все значения с цифрой 1
for k in sorted_dict.keys():                      #перебираем ключи в отсортированном словаре
    if sorted_dict[k] != 1:                       #если значение ключе не равно 1...
        onesexcluded_dict[k] = sorted_dict[k]     #...то кладем эту пару ключ:значение в новый словарь

print("Слова и количества их повторений:")
for eo in onesexcluded_dict.items():
    print(eo)


def rtrn(z):
    if z in sorted_dict:
        w = sorted_dict.get(z)
        print("Слово '" + z + "' встречается в словаре '" + str(w) + "' раз(а).")
        g = rtrn(input("Введите слово, которое хотите посчитать, или введите 'stop' для завершения: "))
    elif z == "stop":
        print("Программа завершена.")
        exit()
    elif z not in sorted_dict:
        print("Слово '" + z + "' отсутствует в словаре")
        g = rtrn(input("Введите слово, которое хотите посчитать, или введите 'stop' для завершения: "))



z = rtrn(input("Введите слово, которое хотите посчитать, или введите 'stop' для завершения: "))
