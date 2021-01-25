import pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

file_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_alphabet = {row.letter: row.code for (key, row) in file_csv.iterrows()}
print(dict_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [dict_alphabet[letter] for letter in word]
print(output_list)
