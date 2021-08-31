import sys

sys.setrecursionlimit(8000)
'''Отменяет предел глубины рекусрии'''

known = {0:0, 1:1}


def fibonacci(n):
    '''
    Считает число фибоначи с помощью рекурсии. Записывает результат в known, причем всю цепочку, то есть если мы посчитали
    число 15, то все числа до 15 тоже попадут в known. При последующем вызове (консолью) глубина рекурсии снижается,
    так как уже поссчитанные значения достаются из known.
    '''
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


print(fibonacci(5000))