list = [0, 1]
f = int(input())

if f == 0:
    print(0)
elif f == 1:
    print(1)
elif f == 2:
    print(3)
else:
    for i in range(f-2):
        list.append(list[i] + list[i+1])
    print(list[-1])