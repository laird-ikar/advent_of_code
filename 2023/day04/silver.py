#!python3

import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 silver.py input.txt")
		return
	with open(sys.argv[1]) as f:
		total = 0
		for line in f:
			words = line.split()
			i = 2
			winning = []
			while words[i] != "|":
				winning.append(words[i])
				i += 1
			nb_victories = 0
			while i < len(words):
				if winning.count(words[i]) == 1:
					nb_victories += 1
				i += 1
			if nb_victories >= 1:
				print(f"Ligne {line} : {nb_victories} victoires ({winning})")
				total += 2 ** (nb_victories - 1)
		print(total)

if __name__ == "__main__":
	main()
