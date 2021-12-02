import sys
import os

test_text = '''199
200
208
210
200
207
240
269
260
263'''

def get_increases(depths):
	last = None
	increases = 0
	for i in depths:
		if i > last and last is not None:
			increases += 1
		last = i
	return increases

def get_window_increases(depths):
	last = None
	increases = 0
	for i in xrange(0,len(depths) -2):
		s = depths[i]+depths[i+1]+depths[i+2]
		if s > last and last is not None:
			increases += 1
		last = s
	return increases

if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	depths = [int(i) for i in input_text.splitlines()]
	print "part 1 increases", get_increases(depths)
	print "part 2 window increases", get_window_increases(depths)