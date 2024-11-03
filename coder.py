# coder
import random

def shuffle_string(s):
    """
    Shuffles the letters in the given string.
    
    Args:
    s (str): The string to shuffle.
    
    Returns:
    str: A new string with the characters of the input string shuffled.
    
    Note:
    - This function keeps spaces in their original positions.
    - Non-letter characters (like punctuation) are treated like letters.
    """
    # Split the string into words
    words = s.split()
    
    # Shuffle each word
    shuffled_words = []
    for word in words:
        # Separate letters from non-letter characters
        letters = [char for char in word if char.isalpha() or char.isdigit()]
        non_letters = [char for char in word if not (char.isalpha() or char.isdigit())]
        
        # Shuffle only the letters
        random.shuffle(letters)
        
        # Reconstruct the word
        shuffled_word = []
        letter_index = 0
        for char in word:
            if char.isalpha() or char.isdigit():
                shuffled_word.append(letters[letter_index])
                letter_index += 1
            else:
                shuffled_word.append(char)
        
        shuffled_words.append(''.join(shuffled_word))
    
    # Join the words back into a string
    return ' '.join(shuffled_words)

def get_code_string():
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	return shuffle_string(alphabet)


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


l_alphabet = get_code_string()
print(l_alphabet)
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