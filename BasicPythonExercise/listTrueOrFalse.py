def is_first_and_last_element_is_true(list_of_number):
    first_element = list_of_number[0]
    last_element = list_of_number[-1]
    if first_element == last_element:
        return True
    else:
        return False


list1 = [10, 20, 30, 40, 10]
print('result is', is_first_and_last_element_is_true(list1))
