from random import randint as ri

list = []
for i in range(0,100):
    list.append(ri(0, 100_000))
sorted_list = list
element = 6
index = 1

for i in range(len(list)):
    if list[i] == element:
        break
i = index
print(index)