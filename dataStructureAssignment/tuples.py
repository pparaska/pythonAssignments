sampleList = [87, 52, 44, 53, 54, 87, 52, 53]

print('sample list', sampleList)

sampleSet = set(sampleList)
sampleList = list(sampleSet)
print('unique items', sampleList)

tuple = tuple(sampleList)
print("tuple ", tuple)

print("Minimum number : ", min(tuple))
print("Maximum number : ", max(tuple))
