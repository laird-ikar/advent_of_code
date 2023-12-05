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
				numbers = line.split()
				for start, lenght in zip(numbers[::2], numbers[1::2]):
					data.append([[int(start), int(start) + int(lenght)], 0])
				continue
			numbers = line.split()
			dest_start = int(numbers[0])
			src_start = int(numbers[1])
			src_end = int(numbers[1]) + int(numbers[2])
			next_data = []
			for d in data:
				if d[1] == 1:
					next_data.append(d)
					continue
				before = [d[0][0], max(d[0][0], min(d[0][1], src_start))]
				overlaping = [
					max(d[0][0], min(d[0][1], src_start)),
					min(d[0][1], max(d[0][0], src_end))]
				after = [min(d[0][1], max(d[0][0], src_end)), d[0][1]]
				overlaping = [dest_start + overlaping[0] - src_start, dest_start + overlaping[1] - src_start]
				print(f"With the range {src_start} to {src_end}, {d[0]} becomes {before if before[0] != before[1] else []}, {overlaping if overlaping[0] != overlaping[1] else []}, {after if after[0] != after[1] else []}")
				if before[0] != before[1]:
					next_data.append([before, 0])
				if overlaping[0] != overlaping[1]:
					next_data.append([overlaping, 1])
				if after[0] != after[1]:
					next_data.append([after, 0])
			data = next_data.copy()
			print(f"Resulting in {data}")
		print(min([d[0][0] for d in data]))

if __name__ == "__main__":
	main()
