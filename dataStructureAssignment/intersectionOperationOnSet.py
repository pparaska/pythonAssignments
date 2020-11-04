firstSet = {65, 42, 78, 83, 23, 57, 29}
secondSet = {67, 73, 43, 48, 83, 57, 29}

print('First Set ', firstSet)
print('Second Set ', secondSet)

intersectionSet = firstSet.intersection(secondSet)

print('Intersection is ', intersectionSet)

for element in intersectionSet:
    firstSet.remove(element)

print('First Set after removing common element ', firstSet)

