originalList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print('Original list ', originalList)

count = dict()
for element in originalList:
    if element in count:
        count[element] += 1
    else:
        count[element] = 1

print('Printing count of each item  ', count)
