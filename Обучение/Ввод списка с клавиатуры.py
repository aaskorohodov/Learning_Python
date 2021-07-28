e = list(input().split())

def numberiffication(x):
    return int(x)

b = list(map(numberiffication, e))

print(b)


l = list(map(int, input().split()))  # map имеет 2 аргумента внутри. Она берет первый и проводит его над всеми значениями второго. Тут она берет строчные значения цифер и перегоняет их в цифры.
print(l)