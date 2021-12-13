import sys
import os
import re

test_text = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''


def part1(text,to_fold=None):
	dots,folds = text.split('\n\n')
	t = []
	for l in folds.splitlines():
		r = re.match(r'fold along ([xy])=(\d+)', l)
		h = (r.group(1) == 'y')
		c = int(r.group(2))
		t.append((h, c))
	pos = set()
	for d in dots.splitlines():
		p = tuple([int(i) for i in d.split(',')])
		for i in xrange(to_fold or len(t)):
			if p[t[i][0]] > t[i][1]:
				u = t[i][1] - (p[t[i][0]] - t[i][1])
				p = ((u, p[1]),(p[0], u))[t[i][0]]
		pos.add(p)
	return len(pos)


def part2(text,to_fold=None):
	dots,folds = text.split('\n\n')
	t = []
	for l in folds.splitlines():
		r = re.match(r'fold along ([xy])=(\d+)', l)
		h = int(r.group(1) == 'y')
		c = int(r.group(2))
		t.append((h, c))
	pos = {}
	max_x = 0
	max_y = 0
	for d in dots.splitlines():
		p = tuple([int(i) for i in d.split(',')])
		for i in xrange(to_fold or len(t)):
			if p[t[i][0]] > t[i][1]:
				o=p
				u = t[i][1] - (p[t[i][0]] - t[i][1])
				p = ((u, p[1]),(p[0], u))[t[i][0]]
		pos[p] = '#'
		max_x = max(p[0], max_x)
		max_y = max(p[1], max_y)
	for i in xrange(max_y+1):
		print ''.join([pos.get((j,i),' ') for j in xrange(max_x+1)])
	return len(pos.values())


if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	t = part1(input_text,1)
	print "part1: ", t
	t = part2(input_text)
	print "part2: ", t
