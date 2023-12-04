#!python3

import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 silver.py input.txt")
		return
	with open(sys.argv[1]) as f:
		lines = f.readlines()
		nb_lines = [1] * len(lines)
		for line in lines:
			words = line.split()
			index = int(words[1][:-1]) - 1
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
			for j in range(nb_victories):
				nb_lines[index + j + 1] += nb_lines[index]
		print(sum(nb_lines))

if __name__ == "__main__":
	main()

# Note:
# I tried to create a queue of the lines, increasing at each victory, but it was too slow.
# So I juste used the fact that you can only add copies of the lines AFTER the current one.
