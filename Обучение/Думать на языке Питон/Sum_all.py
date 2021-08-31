def sumall(*args):
    '''Суммирует любое число переданных агрументов'''
    sum = 0
    tup = tuple(args)
    for el in tup:
        sum += el
    print(sum)