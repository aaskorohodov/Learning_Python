l = list(map(int, input().split()))

total = 0

for x in reversed(l):
    if x < 0:
        total += x
    else:
        break

print(total)