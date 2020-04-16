import re


def baum_seq(n):
	'''
	In mathematics, the Baum–Sweet sequence is an infinite automatic sequence of
	0s and 1s defined by the rule:
		- b_n = 1 if the binary representation of n contains no block of
			consecutive 0s of odd length;
    	- b_n = 0 otherwise;
	for n >= 0.
	'''
	seq = []
	for i, digit in enumerate(range(1, n+1)):
		odd_block = False
		digits = f"{digit:b}"
		zeros = re.findall(r'0+', digits)
		for match in zeros:
			if len(match) % 2 != 0:
				odd_block = True
				break

		if not odd_block:
			seq.append(1)
		else:
			seq.append(0)
	return seq


def baum_seq_alt(n):
	for i in range(1, n+1):
		isValid = len([i for i in list(filter(None, str(bin(i))[2:].split('1'))) if len(i) % 2 != 0])
		yield 1 if isValid == 0 else 0


if __name__ == '__main__':
	res = baum_seq(20)
	print(res)
	res2 = baum_seq_alt(20)
	print(list(res2))