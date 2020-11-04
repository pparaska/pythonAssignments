originalList = [34, 54, 67, 89, 11, 43, 94]

print('Original list ', originalList)

remove_element_at_fourth_index = originalList.pop(4)

print('List After removing element at index 4', originalList)

originalList.insert(2, remove_element_at_fourth_index)
print('List after Adding element at index 2 ', originalList)

originalList.append(remove_element_at_fourth_index)
print('List after Adding element at last ', originalList)
