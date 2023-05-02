# Create a function that takes two lowercase strings str1 and str2 of letters from a to z and returns the sorted and longest string containing distinct letters.


def longest_string(str1, str2):
	string = set(str1 + str2)
	s = sorted(string)
	return "".join(s)
