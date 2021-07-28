a = [1,2,3,4,5,5]

b = set(a)
print(b)

sum1 = 0
for eo in b:
    sum1 += eo
print(sum1)

print(sum(set(a)))