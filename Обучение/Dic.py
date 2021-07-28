d = {"Alex": 25, "Petr": 37}

print(d)

print(len(d))

d["Kate"] = 18

print(d)

print(d["Petr"])

print(d["Kate"])
d["Kate"] = 24
print(d["Kate"])

print(d)

d[10] = 20

print(d)

for k, v in d.items():
    print(k)
    print(v)


for key, value in d.items():
    print("КЛЮЧ: " + str(key) + ", ВОЗРАСТ: " + str(value))