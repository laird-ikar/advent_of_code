#!python3

import sys

def get_numer(str):
	if str[0].isdigit():
		return int(str[0])
	if str.startswith("one"):
		return 1
	if str.startswith("two"):
		return 2
	if str.startswith("three"):
		return 3
	if str.startswith("four"):
		return 4
	if str.startswith("five"):
		return 5
	if str.startswith("six"):
		return 6
	if str.startswith("seven"):
		return 7
	if str.startswith("eight"):
		return 8
	if str.startswith("nine"):
		return 9
	return -1

def main():
	if len(sys.argv) < 2:
		print("Usage: python trebuchet.py <path>")
		return
	path = sys.argv[1]
	with open(path, "r") as f:
		total = 0
		for line in f:
			# find firrst digit in line
			i = 0
			while i < len(line) and get_numer(line[i:]) == -1:
				i += 1
			# find last digit in line
			j = len(line) - 1
			while j >= 0 and get_numer(line[j:]) == -1:
				j -= 1
			param = int(get_numer(line[i:])) * 10 + int(get_numer(line[j:]))
			print(param)
			total += param
		print(total)


if __name__ == "__main__":
	main()
