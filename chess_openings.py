import requests
from collections import Counter
import re

def get_openings(list_of_openings,games_dict):
    for i in range(len(games_dict['games'])):
        _str = games_dict['games'][i]['pgn']
        idx = _str.find('ECOUrl')
        str1 = _str[idx:]
        str2 = str1[:str1.find(']')]
        #print(str2)
        str3 = str2[str2.rindex('/')+1:]
        list_of_openings.append(str3)
    if len(list_of_openings)>0:
        list_of_openings = remove_characters_with_number_and_replace(list_of_openings)
        list_of_openings = remove_non_alphabet_and_replace(list_of_openings)
        most_common = most_common_element(list_of_openings)
        if most_common is not None:
            most_common = add_space(most_common)
            #print(most_common)
            return most_common

def add_space(most_common): #add spaces to the opening name
    new_string = ''
    for i,letter in enumerate(most_common):
        if i and letter.isupper():
            new_string +=' '
        new_string += letter
    return new_string

def process_string(string):
    new_string = ''
    for char in string:
        if not char.isdigit():
            new_string += char
        else:
            break  # Stop adding characters if a number is encountered
    new_string = new_string.replace('-', ' ')  # Replace '-' with space
    return new_string

def remove_characters_with_number_and_replace(input_list):
    output_list = []
    for string in input_list:
        modified_string = process_string(string)
        output_list.append(modified_string)
    return output_list

def process_string1(string):
    # Remove non-alphabet characters and replace '-' with space
    new_string = re.sub(r'[^a-zA-Z\-]', '', string).replace('"', ' ')
    return new_string

def remove_non_alphabet_and_replace(input_list):
    output_list = []
    for string in input_list:
        modified_string = process_string1(string)
        output_list.append(modified_string)
    return output_list

def most_common_element(input_list):
    # Count occurrences of each element in the list
    count_dict = Counter(input_list)
    # Find the most common element and its count
    most_common = count_dict.most_common(1)
    return most_common[0][0]

