def number_divisible_by_five(list_of_number):
    print('Given list is ', list_of_number)
    print('Divisible of 5 in a list')
    for number in list_of_number:
        if number % 5 == 0:
            print(number)


numberList = [10, 20, 33, 46, 55]
number_divisible_by_five(numberList)
