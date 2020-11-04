listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

print('Element at odd-index positions from list one')

elements_at_odd_index_of_listOne = listOne[1::2]
print(elements_at_odd_index_of_listOne)

print('Element at even-index positions from list one')

elements_at_even_index_of_listTwc = listTwo[0::2]
print(elements_at_even_index_of_listTwc)

thirdList = elements_at_odd_index_of_listOne + elements_at_even_index_of_listTwc

print('Printing Final third list')
print(thirdList)
