#!python3

import sys

def has_symbol(string):
	print(f"Checking {string}")
	for char in string:
		if char != "." and not char.isdigit():
			return True
	return False

def main():
	if len(sys.argv) < 2:
		print("Usage: python gear_ratio.py <path>")
		return
	path = sys.argv[1]
	with open(path, "r") as f:
		text = []
		for line in f:
			text.append(line.strip())
		total = 0
		for i in range(len(text)):
			line = text[i]
			j = 0
			while j < len(line):
				char = line[j]
				if char != "*":
					j += 1
					continue
				nbs = []

				# Check left
				if line[j - 1].isdigit():
					start_index = j - 1
					while start_index >= 0 and line[start_index].isdigit():
						start_index -= 1
					nbs.append(int(line[start_index + 1:j]))
				# Check right
				if line[j + 1].isdigit():
					end_index = j + 1
					while end_index < len(line) and line[end_index].isdigit():
						end_index += 1
					nbs.append(int(line[j + 1:end_index]))
				# Check top
				if i > 0 and text[i - 1][j].isdigit():
					start = j
					while start >= 0 and text[i - 1][start].isdigit():
						start -= 1
					end = j
					while end < len(text[i - 1]) and text[i - 1][end].isdigit():
						end += 1
					nbs.append(int(text[i - 1][start + 1:end]))
				else:
					if i > 0 and j > 0 and text[i - 1][j - 1].isdigit():
						start = j - 1
						while start >= 0 and text[i - 1][start].isdigit():
							start -= 1
						nbs.append(int(text[i - 1][start + 1:j]))
					if i > 0 and j < len(text[i - 1]) - 1 and text[i - 1][j + 1].isdigit():
						end = j + 1
						while end < len(text[i - 1]) and text[i - 1][end].isdigit():
							end += 1
						nbs.append(int(text[i - 1][j + 1:end]))
				# Check bottom
				if i < len(text) - 1 and text[i + 1][j].isdigit():
					start = j
					while start >= 0 and text[i + 1][start].isdigit():
						start -= 1
					end = j
					while end < len(text[i + 1]) and text[i + 1][end].isdigit():
						end += 1
					nbs.append(int(text[i + 1][start + 1:end]))
				else:
					if i < len(text) - 1 and j > 0 and text[i + 1][j - 1].isdigit():
						start = j - 1
						while start >= 0 and text[i + 1][start].isdigit():
							start -= 1
						nbs.append(int(text[i + 1][start + 1:j]))
					if i < len(text) - 1 and j < len(text[i + 1]) - 1 and text[i + 1][j + 1].isdigit():
						end = j + 1
						while end < len(text[i + 1]) and text[i + 1][end].isdigit():
							end += 1
						nbs.append(int(text[i + 1][j + 1:end]))
				if len(nbs) == 2:
					total += nbs[0] * nbs[1]
				else:
					for k in range(-1, 2):
						print(text[i + k][j - 3:j + 4])
					print(nbs)
				j += 1
		print(total)
if __name__ == "__main__":
	main()
