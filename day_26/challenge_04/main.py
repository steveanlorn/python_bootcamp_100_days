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

word = input("Input a word: ")
output = [nato_phonetic_dic[letter.lower()] for letter in word]
print(output)
