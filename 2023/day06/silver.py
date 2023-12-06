#!python3

import sys
from math import sqrt, floor, ceil

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 silver.py input.txt")
		return
	with open(sys.argv[1]) as f:
		res = 1
		lines = f.readlines()
		times = [int(line) for line in lines[0].split()[1:]]
		dists = [int(line) for line in lines[1].split()[1:]]
		for i in range(len(times)):
			nb_victories = 0
			a = 1
			b = -times[i]
			c = dists[i]
			mini = ceil((-b - sqrt(b**2 - 4*a*c)) / (2*a))
			maxi = floor((-b + sqrt(b**2 - 4*a*c)) / (2*a))
			print(mini, maxi)
			nb_victories = maxi - mini + 1
			if mini ** 2 - times[i] * mini + dists[i] >= 0:
				nb_victories -= 1
			if maxi ** 2 - times[i] * maxi + dists[i] >= 0:
				nb_victories -= 1
			print(nb_victories)
			res *= nb_victories
		print(res)

if __name__ == "__main__":
	main()

# We are looking for
# the number of x in N such that
# x(t - x) > d
# <=> x^2 - tx + d < 0
# Aka x in (mini, maxi) since a > 0
