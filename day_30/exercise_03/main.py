# Nato Alphabet Project
# input: a word
# output: its Nato phonetic alphabet
#
# example:
# input: steve
# output: Sierra, Tango, Echo, Victor, Echo

import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dic = {value.letter.lower(): value.code for (key, value) in nato_data_frame.iterrows()}

is_correct_input = False
while not is_correct_input:
    try:
        word = input("Input a word: ")
        output = [nato_phonetic_dic[letter.lower()] for letter in word]
    except KeyError:
        print("Please insert only alphabet")
    else:
        print(output)
        is_correct_input = True
