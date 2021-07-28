a = ["Hey", "Hello", "Goodbye"]

print(a[0])
print(a[1])
print(a[2])

for element in a:
    print(element)

b = [20, 30, 50, 60]
for num in b:
    print(num)
    print(num)

total_sum = 0
for e in b:
    total_sum = total_sum + e
print(total_sum)

range(1, 5)
print(list(range(1, 5)))

for i in range(1, 5):
    print(i)

total_sum2 = 0
for i in range(1, 5):
    total_sum2 += i

print(total_sum2)

print(list(range(1,100)))

5 % 3

total_sum3 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total_sum3 += i

print(total_sum3)


def my_function(n, k):
    if n > 20:
        return 0
        print("Число n больше 20!")
    if n <= 20:
        total_sum_n = 0
        for i in range(1, n+1):
            if i % 2 == 0:
                total_sum_n += i**k
        print(total_sum_n)

