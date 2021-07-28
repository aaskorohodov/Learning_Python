l1 = input().split(" ")

print(l1)

l = []

def is_digit(a):
    if a.isdigit():
       return True
    else:
        try:
            float(a)
            return True
        except ValueError:
            return False

for y in l1:
    if is_digit(y) == True:
        l.append(int(y))
    elif is_digit(y) == False:
        l.append(str(y))

print(l)


dict = {}
temp = None

for x in l:
    if type(x) == str:
        dict[x] = []
        temp = x
    else:
        dict[temp].append(x)

print(dict)

# l = ["Tom", 1, 2, 3, "Kate", 40, 50, 60, "Bob", -50]


#for y in l1:
#    if y.isdigit():
#        l.append(int(y))
#    elif type(y) == str:
#        l.append(str(y))