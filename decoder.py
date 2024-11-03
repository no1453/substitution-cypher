# coder
import random

def get_code_value(char):
	"""
	Returns the integer value of an alphabetical characacter
	Args:
	char (str): A single character string.

	Returns:
	int: The integer value (0-25) of the character

	Raises:
	ValueError: If the input is not a single alphabetical character.
	"""
	# Ensure the input is a single character
	if len(char) != 1:
		raise ValueError("Input must be a single character")
	
	# Check if the character is alphabetical
	if not char.isalpha():
		raise ValueError("Input must be an alphabetical character")
	
	# Convert to lowercase for a consistent 0-25 range
	char = char.lower()
	
	# ASCII value of 'a' is 97, so subtract 97 to get 0-25 range
	return ((ord(char) - 97))

code_alphabet = input()
#code_alphabet = code_alphabet[:-1]
if len(code_alphabet) != 26:
	print("Raising Hell: code len is ", len(code_alphabet))
	exit(-1)

l_alphabet="abcdefghijklmnopqrstuvwxyz"
i = 0
code_dict = {}
for letter in l_alphabet:
	code_dict[code_alphabet[i]] = letter
	i = i + 1

#print(code_dict)

this_code_alphabet = ''
i = 0
for letter in l_alphabet:
	this_code_alphabet = this_code_alphabet + code_dict.get(letter)
	i = i + 1

#print("IAlphabet: [", code_alphabet, "]")
#print("CAlphabet: [", this_code_alphabet, "]")
l_alphabet = this_code_alphabet
u_alphabet = l_alphabet.upper()

line = input()
while True:
	for c in line:
		if c.islower():
			print(  l_alphabet[get_code_value(c)]  , end='')
		elif c.isupper():
			print(  u_alphabet[get_code_value(c)]  , end='')
		else:
			print(c, end='')
	print()
	try:
		line = input()
	except EOFError:
		break