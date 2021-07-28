print("")

list = list(map(int, input("Введите список цифер через порбел: ").split()))

print("")

total = 0
i = 0

while i < len(list):
    if list[i] > 0:
        print("Смотрим место в списке № " + str(i + 1) + ". В нем стоит число " + str(list[i]))
        print("Число " + str(list[i]) + " положительное, пропускаем его")
        print("")
        i += 1
    else:
        total += list[i]
        print("Смотрим место в списке № " + str(i + 1) + ". В нем стоит число " + str(list[i]))
        print("Берем число " + str(list[i]) + " и кладем в общую сумму")
        print("В сумме получается " + str(total))
        print("")
        i += 1


print("Всего получилось " + str(total))