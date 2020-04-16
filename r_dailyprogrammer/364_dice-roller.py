from random import randint


def roll_dice(hand):
	rolls = []
	num_die, num_sides = map(int, hand.split('d'))
	for roll in range(num_die):
		rolls.append(randint(1, num_sides+1))
	print(f"{sum(rolls)}: {' '.join(map(str, rolls))}\n")


if __name__ == '__main__':
	test_input = ["5d12", "6d4", "1d2", "1d8", "3d6", "4d20", "100d100"]
	for hand in test_input:
		roll_dice(hand)

	# bonus
	print("\nBonus:")
	hand = None
	while hand != "quit":
		hand = input("\nGive me a dice roll. Type 'quit' to quit\n")
		roll_dice(hand)