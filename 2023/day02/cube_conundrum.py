#!python3

import sys

def main():
	if len(sys.argv) < 2:
		print("Usage: python cube_conundrum.py <path>")
		return
	path = sys.argv[1]
	with open(path, "r") as f:
		total = 0
		for line in f:
			is_viable = True
			id = int(line[5:line.find(":")])
			line = line[line.find(":") + 1:]
			max_blue = 0
			max_red = 0
			max_green = 0
			print(f"Game {id}")
			for test in line.split(";"):
				test = test.strip()
				for color in test.split(","):
					if color.endswith("blue"):
						nb = int(color[:color.rfind(" ") + 1].strip())
						if nb > max_blue:
							max_blue = nb
					if color.endswith("red"):
						nb = int(color[:color.rfind(" ") + 1].strip())
						if nb > max_red:
							max_red = nb
					if color.endswith("green"):
						nb = int(color[:color.rfind(" ") + 1].strip())
						if nb > max_green:
							max_green = nb
			total += max_blue * max_red * max_green
		print(total)
	return 0

if __name__ == "__main__":
	main()
