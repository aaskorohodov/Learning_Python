dict = {
"a" : 5,
"b" : 4,
"c" : 3,
"d" : 3
}

sorted_values = sorted(dict.values())
sorted_dict = {}

for i in sorted_values:                    #берем отсортированные значения...
    for v in dict.keys():                  #...и идем с ним по всем ключам в исходном словаре
        if dict[v] == i:                   #если ключ в исходном словаре совпал с отсортированным значением...
            sorted_dict[v] = dict[v]       #...то стави совпавший клю в новый словар и присваиваем ему значение их исходного словаря

print(sorted_dict)