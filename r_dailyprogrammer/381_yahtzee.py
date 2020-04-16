"""
You are given a Yahtzee dice roll, represented as a sorted list of 5 integers, each of which is between 1 and 6 inclusive.
Your task is to find the maximum possible score for this roll in the upper section of the Yahtzee score card.

Optional Bonus:
Efficiently handle inputs that are unsorted and much larger, both in the number of dice and in the number of sides per die.

Try to find a solution that's linear (O(N)) in both time and space requirements.
"""

from collections import defaultdict


def yahtzee_upper(rolls):
	scores = defaultdict(lambda: 0)
	for item in rolls:
		scores[item] += 1
	tallies = {num: count*num for (num, count) in scores.items()}
	max_num = max(scores, key=lambda x: scores[x]*x)
	return f"select {max_num} for a score of {scores[max_num]*max_num}"


def test():
	BASIC_TEST = True
	LARGE_TEST = True

	ans_6side = [10, 4, 6, 5, 30]
	tests_6side = [
		[2, 3, 5, 5, 6],
		[1, 1, 1, 1, 3],
		[1, 1, 1, 3, 3],
		[1, 2, 3, 4, 5],
		[6, 6, 6, 6, 6]]

	ans_large = 123456
	tests_large = [
		1654, 1654, 50995, 30864, 1654, 50995, 22747,
		1654, 1654, 1654, 1654, 1654, 30864, 4868,
		1654, 4868, 1654, 30864, 4868, 30864]

	if BASIC_TEST:
		for i, roll in enumerate(tests_6side):
			print(yahtzee_upper(roll))
	if LARGE_TEST:
		print(yahtzee_upper(tests_large))


if __name__ == '__main__':
	test()
