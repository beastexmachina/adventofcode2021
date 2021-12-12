import sys
import os
import re

test_text = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

test_text2 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''

test_text3 ='''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''

class Cave:
	def __init__(self, name, conns=None):
		self.name = name
		self.big = self.name.isupper()
		self.conns = conns if conns else []
	def __repr__(self):
		return 'Cave(%s)' % (self.name)
	def __str__(self):
		return 'Cave(%s,[%s])' % (self.name,','.join([i.name for i in self.conns]))

def part1(text):
	caves = {}
	paths = []
	for l in text.splitlines():
		n1,n2 = l.split('-')
		c1 = caves.get(n1)
		if not c1:
			c1 = Cave(n1)
			caves[n1]=c1
		c2 = caves.get(n2)
		if not c2:
			c2 = Cave(n2)
			caves[n2]=c2
		c1.conns.append(c2)
		c2.conns.append(c1)
	#print '\n'.join(str(c) for c in caves.values())
	todo = [('start',caves['start'])]
	while len(todo):
		prefix,cur = todo.pop()
		for c in cur.conns:
			if c.name == 'end':
				paths.append(','.join((prefix,c.name)))
			elif c.big or not c.name in prefix:
				todo.insert(0,(','.join((prefix,c.name)),c))
	#print paths
	return paths

def part2(text):
	caves = {}
	paths = []
	for l in text.splitlines():
		n1,n2 = l.split('-')
		c1 = caves.get(n1)
		if not c1:
			c1 = Cave(n1)
			caves[n1]=c1
		c2 = caves.get(n2)
		if not c2:
			c2 = Cave(n2)
			caves[n2]=c2
		c1.conns.append(c2)
		c2.conns.append(c1)
	todo = [('start',caves['start'],True)]
	while len(todo):
		prefix,cur,clean = todo.pop()
		for c in cur.conns:
			if c.name == 'end':
				paths.append(','.join((prefix,c.name)))
			elif c.big or not c.name in prefix:
				todo.insert(0,(','.join((prefix,c.name)),c,clean))
			elif clean and c.name != 'start':
				todo.insert(0,(','.join((prefix,c.name)),c,False))
	#print paths
	return paths



if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	elif len(sys.argv) == 1 or sys.argv[1] == 'test2':
		input_text = test_text2
	elif len(sys.argv) == 1 or sys.argv[1] == 'test3':
		input_text = test_text3
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	t = part1(input_text)
	print "part1: ", len(t)
	t = part2(input_text)
	print "part2: ", len(t)

