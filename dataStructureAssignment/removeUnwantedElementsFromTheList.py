rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 47}

for value in rollNumber:
    if value in sampleDict.values():
        rollNumber
    else:
        rollNumber.remove(value)
print('after removing unwanted elements from the list', rollNumber)