import sys
import os
import re

test_text = '''16,1,2,0,4,2,7,1,2,14'''


def part1(crabs):
	costs = [(i,sum([abs(c-i) for c in crabs])) for i in xrange(min(crabs),max(crabs)+1)]
	return min(costs,key=lambda x:x[1])

def part2(crabs):
	costs = [(i,sum([int((abs(c-i)/2.)*(1+abs(c-i))) for c in crabs])) for i in xrange(min(crabs),max(crabs)+1)]
	# (n/2) * (first + end), sum of series
	return min(costs,key=lambda x:x[1])

if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	crabs = [int(i) for i in input_text.split(',')]
	h,c = part1(crabs)
	print "part1: horizontal=%d, cost=%d" % (h,c)
	h,c = part2(crabs)
	print "part2: horizontal=%d, cost=%d" % (h,c)
