# Given a letter and a list of words, return whether the letter does not appear in any of the words.


def forbidden_letter(char, lst):
	findingChrs = any(char in lsts for lsts in lst)
	return not findingChrs
