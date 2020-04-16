from pathlib import Path
from collections import Counter
from itertools import permutations, product


morse_dict = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
	'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
	'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.','o':'---',
	'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
	'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..'}


def main():
	input_path = Path("./inputs/enable1_word_list.txt")
	with open(input_path) as file:
		words = set(line.rstrip() for line in file)
	return {word: smoosh_word(word) for word in words}


def smoosh_word(word):
	morse = ""
	for letter in word:
		morse += morse_dict[letter]
	return morse


if __name__ == '__main__':
	morse_collection = main()

	# bonus 1
	if do := True:
		seq_count = Counter(morse_collection.values())
		print("Bonus 1:")
		seq = next(mseq for (mseq, count) in seq_count.items() if count == 13)
		print(f"\"{seq}\" has 13 occurances")

	# bonus 2
	if do := True:
		print("\nBonus 2:")
		for seq in morse_collection.values():
			if '-'*15 in seq:
				print(f"sequence \"{seq}\" contains 15 dashes")
				break

	# bonus 3
	if do := True:
		print("\nBonus 3:")
		for word, seq in morse_collection.items():
			if len(word) == 21:
				if seq.count('-') == seq.count('.') and \
						word != "counterdemonstrations":
					print(f"{word} is perfectly balanced")
					break

	# bonus 4
	if do := True:
		print("\nBonus 4:")
		for word in filter(lambda x: len(x) == 13, morse_collection):
			seq = morse_collection[word]
			if seq == seq[::-1]:
				print(f"\"{seq}\" is a palindrome")
				break

	# bonus 5
	if do := True:
		print("\nBonus 5:")
		morses = set(filter(lambda x: len(x) == 13, morse_collection.values()))
		all_seqs = {''.join(seq) for seq in product('-.', repeat=13)}
		for seq in all_seqs:
			if seq not in morses:
				print(seq) #logicError only 5 items should print....
			