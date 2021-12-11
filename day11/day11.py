import sys
import os
import re

test_text = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''


def part1(text, steps=100, WIDTH=10,HEIGHT=10):
	flashes = 0
	grid={}
	for i,l in enumerate(text.splitlines()):
		for j,c in enumerate(l):
			grid[(j,i)]=int(c)
	#for i in xrange(HEIGHT):
	#	print ''.join([str(grid[(j,i)]) for j in xrange(WIDTH)])
	for k in xrange(steps):
		todo = []
		done = []
		for j in xrange(HEIGHT):
			for i in xrange(WIDTH):
				todo.append((i,j))
		while len(todo):
			i,j = todo.pop()
			c = grid.get((i,j))
			if c is not None and (i,j) not in done:
				grid[(i,j)] = c + 1
				if grid[(i,j)] > 9:
					todo.extend([(i+l,j-1) for l in xrange(-1,2)])
					todo.extend([(i-1,j),(i+1,j)])
					todo.extend([(i+l,j+1) for l in xrange(-1,2)])
					done.append((i,j))
					flashes += 1
		for d in done:
			grid[d] = 0
		#print "Step: ", k
		#for i in xrange(HEIGHT):
		#	print ''.join([str(grid[(j,i)]) for j in xrange(WIDTH)])
	return flashes

def part2(text, steps=100, WIDTH=10,HEIGHT=10):
	grid={}
	for i,l in enumerate(text.splitlines()):
		for j,c in enumerate(l):
			grid[(j,i)]=int(c)
	k = 0
	while(True):
		k+=1
		todo = []
		done = []
		for j in xrange(HEIGHT):
			for i in xrange(WIDTH):
				todo.append((i,j))
		while len(todo):
			i,j = todo.pop()
			c = grid.get((i,j))
			if c is not None and (i,j) not in done:
				grid[(i,j)] = c + 1
				if grid[(i,j)] > 9:
					todo.extend([(i+l,j-1) for l in xrange(-1,2)])
					todo.extend([(i-1,j),(i+1,j)])
					todo.extend([(i+l,j+1) for l in xrange(-1,2)])
					done.append((i,j))
		for d in done:
			grid[d] = 0
		if len(done) == 10*10:
			return k
	return -1


if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	t = part1(input_text, 100)
	print "part1: ", t
	t = part2(input_text, 100)
	print "part2: ", t

