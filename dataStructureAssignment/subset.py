firstSet = {57, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print('First Set ', firstSet)
print('Second Set ', secondSet)

print('First set is subset of second set -', firstSet.issubset(secondSet))
print('Second set is subset of First set - ', secondSet.issubset(firstSet))

print('First set is Super set of second set - ', firstSet.issuperset(secondSet))
print('Second set is Super set of First set - ', secondSet.issuperset(firstSet))

if firstSet.issubset(secondSet):
    firstSet.clear()

if secondSet.issubset(firstSet):
    secondSet.clear()

print("First Set ", firstSet)
print("Second Set ", secondSet)
