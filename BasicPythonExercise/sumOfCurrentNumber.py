previousNumber = 0
print('Printing current and previous number sum in a given range(10)')
for i in range(10):
    currentSum = previousNumber + i
    print(f'Current Number {i} Previous Number {previousNumber} Sum: {currentSum}')
    previousNumber = i
