import sys
import os
import itertools

test_text = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

DIM = 5

def part1(nums, board_strs):
	#boards = [(dict(i),{}) for i in [[(n,(i,j)) for j,n in enumerate(r.split())] for i,r in enumerate(board_strs.splitlines())]]
	boards = []
	for b_s in board_strs.split('\n\n'):
		b = []
		for i,r in enumerate(b_s.splitlines()):
			b.extend([(n,(i,j)) for j,n in enumerate(r.split())])
		boards.append((dict(b),{}))
	for n in nums.split(','):
		for m,f in boards:
			p = m.get(n)
			if p:
				f[p] = True
				if check(f,p,0) or check(f,p,1):
					total = 0
					for i,p in m.items():
						if not f.get(p):
							total += int(i)
					return int(n), total
	return 0,0

def check(board, pos, by_row):
	for i in xrange(DIM): # check same x
		if not board.get(((pos[0],i),(i,pos[1]))[by_row]):
			return False
	return True


def part2(nums, board_strs):
	#boards = [(dict(i),{}) for i in [[(n,(i,j)) for j,n in enumerate(r.split())] for i,r in enumerate(board_strs.splitlines())]]
	boards = []
	for b_s in board_strs.split('\n\n'):
		b = []
		for i,r in enumerate(b_s.splitlines()):
			b.extend([(n,(i,j)) for j,n in enumerate(r.split())])
		boards.append((dict(b),{}))
	for n in nums.split(','):
		won = []
		for m,f in boards:
			p = m.get(n)
			if p:
				f[p] = True
				if check(f,p,0) or check(f,p,1):
					won.append((m,f))
		for b in won:
			if len(boards) > 1:
				boards.remove(b)
			else:
				total = 0
				for i,p in b[0].items():
					if not f.get(p):
						total += int(i)
				return int(n), total
	return 0,0


if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	nums, _, board_strs = input_text.partition('\n\n')
	n,t = part1(nums, board_strs)
	print "part1: num=%d, total=%d, answer=%d" % (n,t,n*t)
	n,t = part2(nums, board_strs)
	print "part2: num=%d, total=%d, answer=%d" % (n,t,n*t)
