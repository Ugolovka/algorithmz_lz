import random as ran
#сортировка пузырьком
list_1 = [ran.randint(0, 1000000) for t in range(100)] #случайные элементы из указанного диапазона
count1 = 0 #начинаем подсчет с 0 количество сравнений
stop_flag = True # стоп флаг если он имеет значение true запускает цикл
while stop_flag:
    stop_flag = False # меняем значение true, если программа не сделает изменене она завершиться 
    print(list_1) #промежуточный
    for i in range(len(list_1) - 1): # -1 потому что в дальнейшем мы сравниваем с i + 1 
        count1 += 1 #прибавляем каждый цикл +1
        if list_1[i] < list_1[i + 1]: 
            a = list_1[i] 
            list_1[i] = list_1[i + 1] #меняем местами
            list_1[i + 1] = a #меняем местами
            stop_flag = True
#сортировка выбором
list_2 = [ran.randint(0, 1000000) for u in range(100)]
count2 = 0
for i in range(0 ,len(list_2)):
    min = i
    for j in range(i + 1,len(list_2)):
        count2 += 1
        print(list_2) #промежуточный
        if list_2[j] > list_2[min]:
            min = j
    b = list_2[i]
    list_2[i] = list_2[min]
    list_2[min] = b
print(f"Первый отсортированный список:{list_1}")
print(f"Второй отсортированный список:{list_2}") 
print(f'количество сравнений в первом списке:{count1}')
print(f'количество сравнений во втором списке:{count2}')
