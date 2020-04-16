"""
Given a whole-number income amount up to ¤100,000,000,
find the amount of tax owed in Examplania.

Round down to a whole number of ¤
"""

examplania_tax_bracket = {
	10000: 0,
	30000: .1,
	100000: .25,
	None: .4}

def tax_owed(income, bracket_dict):
	"""
	tax bracket info is sent as a dict where:
	key = income cap
	value = tax rate (in decimal format) for income below "a"; 
		"None" is used to signifiy a lack of an income cap
	"""
	dues = 0
	ordered_caps = []
	for cap in bracket_dict:
		if cap != None:
			ordered_caps.append(cap)

	for bracket in ordered_caps:
		if income > bracket:
			dues += bracket_dict[bracket] * bracket
			income -= dues
		else:
			dues += bracket_dict[bracket] * income
			income -= dues
	if income:
		dues += bracket_dict[None] * income
	return int(dues)


if __name__ == '__main__':
	dues = tax_owed(99000000, examplania_tax_bracket)
	print(f"¤{dues} owed")

	# bonus
	print("\nBonus:")