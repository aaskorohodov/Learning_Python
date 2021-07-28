list = [eo * 2 for eo in range(10,1,-1) if eo % 2 != 1]
print(list)

words = ["hello", "hey", 'goodbey', "guitar", "piano"]

words2 = [eo + "." for eo in words if len(eo) < 7]
print(words2)