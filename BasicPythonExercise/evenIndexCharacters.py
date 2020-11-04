givenString = 'pynative'

print("Original String is ", givenString)


def print_char_at_even_index(str):
    for i in range(0, len(str) - 1, 2):
        print(str[i])


print('Printing only even index chars')
print_char_at_even_index(givenString)
