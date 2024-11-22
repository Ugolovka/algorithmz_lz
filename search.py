import random
from random import randint as ri
list_1 = random.sample(range(1000001), 100)#sample позволяет выбрать случайные элементы из указанного диапазона без дубликатов.
print(list_1)

print('ВТОРОЙ СПИСОК')
list_2 = random.sample(range(1000001), 100)#sample позволяет выбрать случайные элементы из указанного диапазона без дубликатов.
list_2.sort()
print(list_2)

el = int(input('искомый элемент:'))

count = 0 #начинаем подсчет с 0 количество сравнений
if el in list_1: #если эле-т находится в list_1
    for i in range(0, len(list_1)):
        count = count + 1 #прибавляем каждый цикл +1
        if list_1[i] == el:
            break 
    print(f'Индекс искомого эл-та из первого списка:{i}')
    print(f'Количество сравнений в линейном поиске:{count}')
else:
    print("Элемент не найден в первом списке")

#бинарный поиск
if el in list_2: #проверка на наличие в списке
    first = 0
    last = len(list_2)-1
    count2 = 0
    index = 1
    while (first <= last) and index == 1:
        mid = (first+last)//2 # индекс элемента в середине списка
        count2 = count2 + 1 #прибавляем каждый цикл +1
        if list_2[mid] == el:
            index = mid
        else: 
            if el<list_2[mid]:
                last = mid -1
            else:
                first = mid +1
    print(f'Количество сравнений в бинарном поиске:{count2}')
    print(f'Индекс искомого эл-та из второго списка:{index}')
else:
    print("Элемент не найден во втором списке")
