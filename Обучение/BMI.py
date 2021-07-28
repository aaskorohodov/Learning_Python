print("Укажите ваше имя, затем нажмите Entr:")
name = input()
print("Укажите ваш рост:")
height = int(input())
print("Укажите ваш вес:")
weight = int(input())

bmi = weight / ((height/100) ** 2)
print("")
print("Ваш индекс массы тела: " + str(bmi))
if bmi < 18.5:
    print("ИМТ ниже 18.5 считается дифицитным")
elif bmi < 25:
    print("ИМТ от 18,5 до 24,9 считается нормой")
else:
    print("ИМТ выше 25 считается избыточным")

print("")
if bmi < 18.5:
    print(name + ", у вас недостаток массы тела, немедленно идите есть.")
elif bmi < 25:
    print(name + ", у вас нет лишнего веса.")
else:
    print(name + ", у вас есть лишний вес.")