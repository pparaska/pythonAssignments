def product(number1, number2):
    result = number1 * number2
    if result < 1000:
        print("Product of two numbers is ", result)
        return result
    else:
        print("Sum of two numbers is ", number1 + number2)
        return number1 + number2


product(20, 30)
