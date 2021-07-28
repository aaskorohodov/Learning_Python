a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
b = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
#это исходные шифровальные данные.

word = 'banana banana'
word2 = 'Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?'
#это переменные для хранения закодированного или обычного текста. Можно сделать сюда input


def list_to_str(list):
    '''Переводит список в строку:
    просто перебирает список и плюсует каждый элемент к строке'''
    cripted = ''

    for eo in list:
        cripted += eo

    return cripted


def encryption(word, frm, to):
    '''Криптование. Создает словарь "encrip" склеивая две строки сверху. ZIP клеит буквы из первой и второй строки.
    задаем пустой список crip, в него будем класть криптованную фразу\слово.
    перебираем переданное функции слово\фразу, если буква встречается в ключах свежесделанного словаря, то добавляем значение слвоаря в строку.
    Или добавляем в неизменном виде (это для знаков припинания и всего того, что не нужно криптовать.
    В конце зовем функцию преобразования в строку и возвращаем что она нам отдаст.
    Чтобы это все заработало в обратном порядке (раскриптовало слово\фразу), надо передать начальные списки a,b в обратном порядке'''
    encrip = dict(zip(frm, to))
    crip = []
    for eo in word:
        if eo in encrip.keys():
            crip.append(encrip.get(eo))
        else:
            crip.append(eo)
    return list_to_str(crip)


print(encryption(word2, b, a))