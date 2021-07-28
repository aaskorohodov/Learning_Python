a = [1,2,3,"asd"]
print(a)

print(a[2])

arr_2d = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(arr_2d)

print(arr_2d[0][2])

arr_2d_2 = [[1,2,3],
            [4,5,6,-1,-5],
            [7]]
print(arr_2d_2)


def print_matrix(x):
    for eo in x:                    #проходим по всем элементам списка
        for el in eo:               #для каждого элемента внутри элемента...
            print(el, end = ' ')    #печатаем вложенный элемент, но через пробел (end = пробел)
        print()                     #после печатаем ничего, но print вставляет переход на новую строку (\n), так что мы переходим на новую строку

print_matrix(arr_2d)

print()

def print_matrix_2(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j], end = ' ')
        print()

print_matrix_2(arr_2d_2)

arr_2d[1][1] = 100

print_matrix(arr_2d)


d_a = []
def create_2d_arr(m, n):
    for i in m:
        for x in n:
            d_a[i][x] = 0

create_2d_arr(3, 4)
print(d_a)