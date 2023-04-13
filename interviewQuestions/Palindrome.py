#Is the String a Palindrome

# A palindrome is a word that is identical forward and backwards.

# Given a word, create a function that checks whether it is a palindrome.


def is_palindrome(txt):
	return txt == txt[::-1]
