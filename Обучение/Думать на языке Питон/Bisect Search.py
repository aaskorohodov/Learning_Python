import bisect
import time

a = [i for i in range(1000)]

def bisect_search(my_list, word):
    index = bisect.bisect(my_list, word)
    if my_list[index - 1] == word:
        print(f'Искомый элемент {word} находится в списке по индексу {index - 1}')
    else:
        print(f"Искомого элемента нет в списке")

#bisect_search(a, 992)
#print(a[992])

steps_sount = 0

def manual_bisect(my_list, word):
    global steps_sount
    steps_sount += 1
    x = len(my_list) // 2
    first_half = my_list[0:x]
    second_half = my_list[x:(x*2)]
    print(first_half, second_half)
    time.sleep(1)
    if first_half[-1] == word:
        print(steps_sount)
        return first_half[-1]
    elif second_half[-1] == word:
        print(steps_sount)
        return second_half[-1]
    elif first_half[-1] > word:
        res = manual_bisect(first_half, word)
        return res
    elif first_half[-1] < word:
        res = manual_bisect(second_half, word)
        return res


print(manual_bisect(a, 249))