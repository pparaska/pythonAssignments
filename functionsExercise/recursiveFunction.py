def calculate_recursive_sum(num):

    if num:
        return num + calculate_recursive_sum(num - 1)
    else:
        return 0


recursive_sum = calculate_recursive_sum(10)
print(recursive_sum)
