#!python3

import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 silver.py input.txt")
		return
	with open(sys.argv[1]) as f:
		data = f.read()
		floor = 0
		count = 0
		for c in data:
			count += 1
			if c == "(":
				floor += 1
			elif c == ")":
				floor -= 1
			if floor == -1:
				break
		print(count)

if __name__ == "__main__":
	main()
