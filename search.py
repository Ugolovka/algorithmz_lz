from random import randint as ri

list = []
for i in range(0,100):
    list.append(ri(0, 100_000))
aim  = 4567

first = 0
last = len(list)-1
index = -1
while (first <= last) and (index == -1):
    mid = (first+last)//2
    if list[mid] == aim:
        index = mid
    else:
        if aim<list[mid]:
            last = mid -1
        else:
            first = mid +1
print(index)
