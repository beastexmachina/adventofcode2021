import sys
import os
import re

test_text = '''3,4,3,1,2'''


def part1(fish, days=80):
	fish = fish[:]
	for i in xrange(days):
		for j in xrange(len(fish)):
			f = fish[j]
			if f == 0:
				fish[j] = 6
				fish.append(8)
			else:
				fish[j] -= 1
	return len(fish)

def part2(init, days=80):
	fish = [0]*9
	for f in init:
		fish[f] = fish[f] + 1
	for i in xrange(days):
		n = fish[0]
		for j in xrange(1,len(fish)):
			fish[j-1]=fish[j]
		fish[6] = fish[6] + n
		fish[-1] = n
	return sum(fish)

if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	fish = [int(i) for i in input_text.split(',')]
	p1 = part1(fish,80)
	print "part1: ", p1
	p2 = part2(fish,256)
	print "part2: ", p2
