from random import randint as ri

list = []
for i in range(0,100):
    list.append(ri(0, 100_000))
unsorted_list = list
sorted_list = []

while len(unsorted_list) > 0:
    min = unsorted_list[0]
    for i in range(0, len(unsorted_list)):
        if unsorted_list[i] > min:
            min = unsorted_list[i]
    sorted_list.append(min)
    unsorted_list.remove(min)

print(sorted_list)