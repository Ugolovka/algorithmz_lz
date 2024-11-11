from random import randint as ri

list = []
for i in range(0,100):
    list.append(ri(0, 100_000))
sorted_list = list
stop_flag = True
while stop_flag is True:
    stop_flag = False
    for i in range(0, len(sorted_list) - 1):
        if sorted_list[i] < sorted_list[i + 1]:
            swap = sorted_list[i]
            sorted_list[i] = sorted_list[i + 1]
            sorted_list[i + 1] = swap
            stop_flag = True

print(sorted_list)
