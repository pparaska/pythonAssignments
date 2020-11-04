def append_second_string_in_the_middle_of_first(string1, string2):
    index_of_middle_character = int(len(string1) / 2)
    print('given strings are', string1, string2)
    three_middle_characters = string1[:index_of_middle_character:] + string2 + string1[index_of_middle_character:]
    print(three_middle_characters)


append_second_string_in_the_middle_of_first('Ault', 'Kelly')