name1 = "Tom"
height1 = 1.90
weight1 = 80

name2 = "Katy"
height2 = 1.70
weight2 = 60

name3 = "Bob"
height3 = 2
weight3 = 150

def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)

    print("Индекс массы тела " + name + ": " + str(bmi))

    if bmi < 25:
        return name + " не имеет лишнего веса"
    else:
        return name + " имеет лишний вес"

bmi1 = bmi_calculator(name1, height1, weight1)
bmi2 = bmi_calculator(name2, height2, weight2)
bmi3 = bmi_calculator(name3, height3, weight3)

print(bmi1)
print(bmi2)
print(bmi3)