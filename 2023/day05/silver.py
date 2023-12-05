#!python3

import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 silver.py input.txt")
		return
	with open(sys.argv[1]) as f:
		res = 0
		mode = 'seed'
		data = []
		while f.readable():
			line = f.readline()
			if line == "":
				break
			if line == "\n":
				continue
			if line == "seed-to-soil map:\n":
				mode = 'soil'
				for d in data:
					d[1] = 0
				continue
			if line == "soil-to-fertilizer map:\n":
				mode = 'fertilizer'
				for d in data:
					d[1] = 0
				continue
			if line == "fertilizer-to-water map:\n":
				mode = 'water'
				for d in data:
					d[1] = 0
				continue
			if line == "water-to-light map:\n":
				mode = 'light'
				for d in data:
					d[1] = 0
				continue
			if line == "light-to-temperature map:\n":
				mode = 'temperature'
				for d in data:
					d[1] = 0
				continue
			if line == "temperature-to-humidity map:\n":
				mode = 'humidity'
				for d in data:
					d[1] = 0
				continue
			if line == "humidity-to-location map:\n":
				mode = 'location'
				for d in data:
					d[1] = 0
				continue
			if mode == 'seed':
				line = line[line.find(":") + 1:]
				for n in line.split():
					data.append([int(n), 0])
				continue
			numbers = line.split()
			src_start = int(numbers[1])
			dest_start = int(numbers[0])
			length = int(numbers[2])
			for d in data:
				if d[1] == 0 and d[0] >= src_start and d[0] < src_start + length:
					d[0] = dest_start + d[0] - src_start
					d[1] = 1
		print(min([d[0] for d in data]))

if __name__ == "__main__":
	main()
