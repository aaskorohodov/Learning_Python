def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def print_hist(h):
    list_sorted = list(h.keys())
    list_sorted.sort()
    for c in list_sorted:
        print (c, ':', h[c])


h = histogram('bcad')
print_hist(h)


my_dict = {'a':10, 'b':10, 'g':5, 'l':10}


def reverse_lookup(d, v):
    '''Поиск ключей по значениям'''
    my_list = []
    for k in d:
        if d[k] == v:
            my_list.append(k)
    return my_list


print(reverse_lookup(my_dict, 10))