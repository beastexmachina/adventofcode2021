import sys
import os

test_text = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''

def new_pos(data):
	m = {'forward':(1,0), 'down':(0,1), 'up':(0,-1)}
	dist = 0
	depth = 0
	for l in data:
		c, v = l.split()
		x = int(v)
		d0,d1 = m[c]
		dist += d0 *x
		depth += d1 *x
	return dist, depth

def new_pos2(data):
	m = {'forward':(0,1,1), 'down':(1, 0, 0), 'up':(-1, 0, 0)}
	a = 0
	h = 0
	d = 0
	for l in data:
		c, v = l.split()
		x = int(v)
		da,dh,dx = m[c]
		a += da * x
		h += dh * x
		d += dx * x * a
	return a,h,d

if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	data = input_text.splitlines()
	dist,depth = new_pos(data)
	print "%d forward, %d down: %d" %(dist, depth, dist * depth)
	a,h,d = new_pos2(data)
	print "%d aim, %d horizontal, %d down: %d" % (a,h,d, h * d)