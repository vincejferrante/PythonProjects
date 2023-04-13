# Create a function that takes a string and returns the letters that occur only once.
# The final list should not include letters that appear more than once in the string.
# Return the letters in the sequence they were originally in, do not sort them.


def find_letters(word):
	Unique_Letters = []
	for letter in word:
		if letter not in Unique_Letters:
			if word.count(letter) == 1:
				Unique_Letters.append(letter)
	return Unique_Letters
