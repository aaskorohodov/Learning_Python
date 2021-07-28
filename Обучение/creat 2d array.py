d_a = []

def create_2d_arr(m, n):

    for i in range(m):
        i_a = []
        for j in range(n):
            i_a.append(0)
        d_a.append(i_a)

a = input().split(" ")

print(a)

b = int(a[0])
c = int(a[1])

create_2d_arr(b,c)

print(d_a)