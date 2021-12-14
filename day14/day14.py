import sys
import os
import re

test_text = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''


def part1(text,steps=10):
	p, instructions = text.split('\n\n')
	m = dict([l.split(' -> ') for l in instructions.splitlines()])
	for i in xrange(steps):
		n = []
		for j in xrange(len(p) - 1):
			n.append(p[j])
			n.append(m[p[j:j + 2]])
		n.append(p[-1])
		p = ''.join(n)
	counts = [(i,p.count(i)) for i in 'NCBH']
	counts.sort(key=lambda x:x[1])
	return counts


def part2(text,steps=10):
	p, instructions = text.split('\n\n')
	m = dict([l.split(' -> ') for l in instructions.splitlines()])
	r = {}
	for j in xrange(len(p) - 1):
		s = p[j:j + 2]
		r[s] = 1 + r.get(s,0)
	for i in xrange(steps):
		n = {}
		for k,c in r.iteritems():
			a = m[k]
			s = k[0] + a
			n[s] = c + n.get(s,0)
			s = a + k[1]
			n[s] = c + n.get(s,0)
		r = n
		#print i,r
	c = {}
	for k,v in r.iteritems():
		for i in k:
			c[i] = v + c.get(i,0)
	c[p[0]] = c[p[0]] + 1 # first char is not duplicated
	c[p[-1]] = c[p[-1]] + 1 # last char is not duplicated
	return sorted([(k,v/2) for k,v in c.iteritems()], key=lambda x:x[1])


if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	a = part1(input_text,10)
	print "part1: ", a," answer=",a[-1][1]-a[0][1]
	a = part2(input_text,40)
	print "part2: ", a," answer=",a[-1][1]-a[0][1]
