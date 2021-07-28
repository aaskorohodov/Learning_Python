a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for elem in a:
    if elem < 5:
        print(elem)



print([elem for elem in a if elem < 5])


b = 0
while a[b] < 5:
    print(a[b])
    b += 1