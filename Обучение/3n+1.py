

count = 0


def _3n_and_1(num):
    global count
    if num == 1:
        print(count)
        count = 0
        inpu()
    elif num % 2 == 0:
        num = num / 2
        count += 1
        _3n_and_1(num)
    else:
        num = num * 3 + 1
        count += 1
        _3n_and_1(num)


def inpu():
    _3n_and_1(int(input()))


inpu()