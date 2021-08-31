a = ['a', 'v', 'a']
b = [1, 2, 3, 5, 4]


def is_sorted(lis):
    i = 0
    for el in lis:
        try:
            if lis[i] <= lis[i+1]:
                i = i + 1
            else:
                return False
        except IndexError:
            pass
    return True

print(is_sorted(a))