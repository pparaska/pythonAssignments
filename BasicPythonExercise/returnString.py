# given a string and an integer number n
# remove characters from a string starting
# from zero upto n and return new string

def remove_characters(given_string, n):
    return given_string[n:]


print('Removing n number of chars')
print(remove_characters('pynative', 4))
