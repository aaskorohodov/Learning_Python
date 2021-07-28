list = [[1,2,3,4],["a","b","c","d"],[7,8,9,10]]

for eo in list:
    eo.reverse()

def print_matrix(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j], end = ' ')
        print()

print_matrix(list)