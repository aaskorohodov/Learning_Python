a = [3, 5, 20]
print(a)

a.append(15)

print(a)

a.append("hi!")
print(a)

a.append([5, 6])
print(a)

a.pop()
print(a)

a.pop()
print(a)

print(a[0])

print(a[3])

print(a[-1])

a[0] = 100
print(a)

a.pop(2)
print(a)

b = ["hello", "goodbye", "hey"]
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)

b[0], b[2] = b[2], b[0]
print(b)

a,b = 1,2
print(a)
print(b)