a = [1,2,3,4,5]
b = []

for i in a:
    b.append(i*2)

print(b)

c = [f*2 for f in a]

print(c)

d = [num *3 for num in range(1,6)]

print(d)

e = []
for i in range (1,6):
    e.append(i*3)

print(e)

a = [1,10,12,4,3,20,55]
b = []
for eo in a:
    if eo <= 10:
        b.append(eo)

print(b)

b = [eo for eo in a if eo < 10]
print(b)

b = [eo**2 for eo in a if eo < 10]
print(b)


words = ["hello","hey", 'goodbey', "guitar", "piano"]
a = [eo for eo in words if len(eo) < 6]
print(a)


