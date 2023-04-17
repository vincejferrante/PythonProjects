# Create a function that takes a list of numbers and returns the second largest number.


def second_largest(lst):
	srt = sorted(lst, reverse=True)
	return srt[1]
