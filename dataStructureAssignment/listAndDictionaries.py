speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

print('Values of dictionary- ', speed.values())

list_of_speed = list()
for value in speed.values():
    if value not in list_of_speed:
        list_of_speed.append(value)
print('list of unique elements', list_of_speed)
