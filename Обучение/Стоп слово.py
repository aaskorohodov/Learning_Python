words = list(input().split())

c = 0

while c < len(words) and words[c] != "stop" :
    print(words[c])
    c += 1








for x in words:
    if x == "stop" or x == "asd":
        break
    print(x)