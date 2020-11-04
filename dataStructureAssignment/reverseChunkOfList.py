sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print('Original list ', sampleList)

chunk1 = sampleList[0:3]
print('Chunk1', chunk1)

chunk1.reverse()
print('After reversing it ', chunk1)

chunk2 = sampleList[3:6]
print('Chunk2', chunk2)
chunk2.reverse()
print('After reversing it ', chunk2)

chunk3 = sampleList[6:9]
print('Chunk3', chunk3)
chunk3.reverse()
print('After reversing it ', chunk3)
