"""
Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.

The criteria for a candidate to be qualified in the coding interview is:

The candidate should have complete all the questions.
The maximum time given to complete the interview is 120 minutes.
The maximum time given for very easy questions is 5 minutes each.
The maximum time given for easy questions is 10 minutes each.
The maximum time given for medium questions is 15 minutes each.
The maximum time given for hard questions is 20 minutes each.
If all the above conditions are satisfied, return "qualified", else return "disqualified".

You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.

Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].

The maximum time to complete the interview includes a buffer time of 20 minutes.
"""

def interview(lst, tot):
	veryEasy = sum(lst[0:2])
	easy = sum(lst[2:4])
	medium = sum(lst[4:6])
	hard = sum(lst[6:8])
	total = sum(lst)
	length = len(lst)
	if veryEasy <= 10 and easy <= 20 and medium <= 30 and hard <= 40 and total <= 120 and tot <= 120 and length == 8:
		return 'qualified'
	else:
		return 'disqualified'
