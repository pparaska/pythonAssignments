def outer_function(a, b):
    def inner_function(a, b):
        return a + b

    addition_of_inner_function = inner_function(a, b)
    return addition_of_inner_function + 5


result = outer_function(5, 10)
print(result)
