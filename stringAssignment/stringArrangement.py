givenString = 'PyNaTive'
lower_characters = []
upper_characters = []
for character in givenString:
    if character.islower():
        lower_characters.append(character)
    else:
        upper_characters.append(character)
sorted_list = (lower_characters + upper_characters)
sorted_string = ''.join(sorted_list)
print(sorted_string)
