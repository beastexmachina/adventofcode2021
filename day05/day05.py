import sys
import os
import re

test_text = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''


def part1(text):
	grid = {}
	for l in input_text.splitlines():
		r = re.match(r'(\d+),(\d+) -> (\d+),(\d+)',l)
		x1,y1,x2,y2 = [int(i) for i in r.groups()]
		if x1 == x2:
			for i in xrange(min(y1,y2),max(y1,y2)+1):
				grid[(x1,i)] = grid.get((x1,i),0) + 1
		elif y1 == y2:
			for i in xrange(min(x1,x2),max(x1,x2)+1):
				grid[(i,y1)] = grid.get((i,y1),0) + 1
	return sum([1 for i in grid.itervalues() if i > 1])

def part2(text):
	grid = {}
	for l in input_text.splitlines():
		r = re.match(r'(\d+),(\d+) -> (\d+),(\d+)',l)
		x1,y1,x2,y2 = [int(i) for i in r.groups()]
		if x1 == x2:
			for i in xrange(min(y1,y2),max(y1,y2)+1):
				grid[(x1,i)] = grid.get((x1,i),0) + 1
		elif y1 == y2:
			for i in xrange(min(x1,x2),max(x1,x2)+1):
				grid[(i,y1)] = grid.get((i,y1),0) + 1
		else:
			i = x1
			j = y1
			dx = (-1,1)[x2>x1]
			dy = (-1,1)[y2>y1]
			for _ in xrange(abs(x2-x1)+1):
				grid[(i,j)] = grid.get((i,j),0) + 1
				i+=dx
				j+=dy
	#for i in xrange(10):
	#	print ''.join([str(grid.get((j,i),'.')) for j in xrange(10)])
	return sum([1 for i in grid.itervalues() if i > 1])

if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	p1 = part1(input_text)
	print "part1: ", p1
	p2 = part2(input_text)
	print "part2: ", p2
