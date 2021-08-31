import random
from random import random

a = 5
print(a + random())


words = [(7, 'goodbye'), (5, 'hello'), (5, 'hellb'), (5, 'hella'), (2, 'hi')]


def test(words):
    randomed = []
    for num, wor in words:
        r = random() + num
        randomed.append((r, wor))

    print(randomed)

    randomed.sort(reverse=True)
    print(randomed)

    words = []
    for num, wor in randomed:
        num = int(num)
        words.append((num, wor))

    print(words)


test(words)