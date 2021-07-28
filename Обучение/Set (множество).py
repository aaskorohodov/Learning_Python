a = set()
print(a)

a = set([1,2,3,4,5,"Hello"])

print(a)

b = {1,2,3,4,5,6,6}
print(b)

a = set()
a.add(1)
print(a)

a.add(2)
a.add(10)
a.add("Hello")
print(a)

a.add(2)

print(a)

a.add("hello")
print(a)

for eo in a:
    print(eo)

my_list = [1,2,1,1,5,'hello']
my_set = set()

for el in my_list:
    my_set.add(el)

print(my_set)

my_set = set(my_list)
print(my_set)

my_list = list(my_set)
print(my_list)

a = {"hello", "hey", 1,2,3}

print(5 in a)

print(15 not in a)


