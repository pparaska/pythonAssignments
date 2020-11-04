def get_three_middle_characters(given_string):
    print('given String is', given_string)
    index_of_middle_character = int(len(given_string) / 2)
    print(
        f'index of middle character is : {index_of_middle_character} and middle character is {given_string[index_of_middle_character]}')
    three_middle_characters = given_string[index_of_middle_character - 1:index_of_middle_character + 2]
    print('Three middle characters are: ', three_middle_characters)


get_three_middle_characters('JhonDipPeta')
