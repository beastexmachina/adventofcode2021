import sys
import os
import operator

test_text = '''2199943210
3987894921
9856789892
8767896789
9899965678
'''


def part1(text):
	WIDTH = text.find('\n')
	HEIGHT = text.count('\n')
	data = {}
	for i,l in enumerate(input_text.splitlines()):
		for j,c in enumerate(l):
			data[(i,j)]=int(c)
	lows = []
	for j in xrange(WIDTH):
		for i in xrange(HEIGHT):
			k = data[(i,j)]
			if k<data.get((i-1,j),0xff) and k<data.get((i,j-1),0xff) and k<data.get((i+1,j),0xff) and k<data.get((i,j+1),0xff):
				lows.append(k)
	return lows

def part2(text):
	WIDTH = text.find('\n')
	HEIGHT = text.count('\n')
	data = {}
	for i,l in enumerate(input_text.splitlines()):
		for j,c in enumerate(l):
			data[(j,i)]=int(c)
	m = {}
	basins = []
	for j in xrange(HEIGHT):
		for i in xrange(WIDTH):
			k = data[(i,j)]
			if k < 9:
				above = m.get((i,j-1))
				left = m.get((i-1,j))
				if above:
					m[(i,j)]=above
					above.add((i,j))
				if left and above and left != above:
					above.update(left)
					for o in left:
						m[o] = above
					basins.remove(left)
				elif left:
					m[(i,j)]=left
					left.add((i,j))
				if not (above or left):
					basins.append(set([(i,j)]))
					m[(i,j)] = basins[-1]
	scores = [len(i) for i in basins]
	scores.sort()
	return scores[-3:]


if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	lows = part1(input_text)
	print "part1: ", lows, sum([1+i for i in lows])
	basins = part2(input_text)
	print "part2: ", basins, reduce(operator.mul, basins)
