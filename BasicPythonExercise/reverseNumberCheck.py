def is_reversed_number_is_same_as_original(given_number):
    print("original number", given_number)
    original_number = given_number
    reversed_number = 0
    while given_number > 0:
        reminder = given_number % 10
        reversed_number = reversed_number * 10 + reminder
        given_number = given_number // 10
    if original_number == reversed_number:
        return True
    else:
        return False


print('The original and reverse number is same:', is_reversed_number_is_same_as_original(121))
