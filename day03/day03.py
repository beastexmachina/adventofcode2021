import sys
import os

test_text = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

def part1(data):
	s = len(data)
	l = len(data[0])
	d = ''.join(data)
	g = int(''.join([('0','1')[(d[i::l].count('1'))>=(s/2.)] for i in xrange(l)]),2)
	e = g ^ (int('1'*l,2))
	return g,e

def count(data,l,i,bias):
	d = ''.join(data)
	t = (('1','0')[bias],('0','1')[bias])
	c = ''.join([t[(d[i::l].count('1'))>=(d[i::l].count('0'))] for i in xrange(l)])
	return c


def part2(data):
	a = data[:]
	b = data[:]
	l = len(data[0])
	#g_s = '{:0{width}b}'.format(g,width=l)
	#e_s = '{:0{width}b}'.format(e,width=l)
	for i in xrange(l):
		if len(a) > 1:
			a_s = count(a,l,i,1)
			a = [j for j in a if j[i] == a_s[i]]
		if len(b) > 1:
			b_s = count(b,l,i,0)
			b = [j for j in b if j[i] == b_s[i]]
	return int(a[0],2),int(b[0],2)

if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	data = input_text.splitlines()
	g,e = part1(data)
	print "%d gamma, %d epsilon, power, %d" %(g,e, g*e)
	a,b = part2(data)
	print "%d O2, %d C02, life_support, %d" %(a,b, a*b)