import time


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
#x = a.remove([a[0]:a[-1]])
#print(a[0])


def cummulative(list):
    res = [1]
    n = 1
    for num in list:
        try:
            res.append(list[n] + list[n-1])
            n += 1
        except IndexError:
            pass
    print(res)


def middle(a):
    x = a[1:-1]
    return x

def chop(a):
    del a[0], a[-1]


def remove_duplicates(lis):
    '''Убирает дупликаты из списка, отдает новый спсок (без дупликатов)'''
    b = []

    for eo in lis:
        if eo not in b:
            b.append(eo)
    return b

file = open('C:\word.txt')
file2 = open('C:\word.txt')


start_time_append = time.time()
lis = []
for eo in file:
    eo = eo.replace('\n', '')
    lis.append(eo)

stop_time_append = time.time()
print(stop_time_append - start_time_append)


star_time_plus = time.time()
t = []
for eo in file2:
    eo = eo.replace('\n', '')
    t = t + [eo]

stop_time_plus = time.time()
print(stop_time_plus - star_time_plus)