my_list = [6, 3, 5, 2, 9]

total = 0
i = 0

while i < len(my_list) and my_list[i] > 0: # len это длина списка, или чего-то другого
    total += my_list[i]
    i += 1

print(total)


i6 = 0

while True:
    if i6 == 100:
        break
    print(i6)
    i6 += 1
