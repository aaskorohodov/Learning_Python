def rot13_to_int(word, rot):
    orded = []
    word = word.lower()
    for eo in word:
        orded.append(ord(eo) + (rot % 26))
    ord_d = []
    for eo in orded:
        if eo > 122:
            eo = eo - 26
            ord_d.append(eo)
        else:
            ord_d.append(eo)
    rot13_to_str(ord_d)

def rot13_to_str(ord_d):
    list = []
    for eo in ord_d:
        eo = chr(eo)
        list.append(eo)
    list2 = ""
    for eo in list:
        list2 += eo
    print(list2)

def rot13_decoding(word, rot):
    orded = []
    word = word.lower()
    for eo in word:
        orded.append(ord(eo) - (rot % 26))
        print(ord(eo))
    print(orded)
    ord_d = []
    for eo in orded:
        if eo < 97:
            eo = eo + 26
            ord_d.append(eo)
        else:
            ord_d.append(eo)
    print(ord_d)
    rot13_to_str(ord_d)


print(ord('i'), ord('n'), ord('v'))


a = 'bananaz z'
b = 'Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN'
rot13_decoding(b, 13)
rot13_to_int(a, 10)