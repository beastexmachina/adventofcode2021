import sys
import os
import re

test_text = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''


def part1(text):
	outs = [i.split('|')[-1] for i in text.splitlines()]
	total = 0
	for i in outs:
		total += sum([1 for j in i.split() if len(j) in [2,4,3,7]])
	return total

def part2(text):
	data = [tuple(i.split('|')) for i in input_text.splitlines()]
	total = 0
	for clues,outs in data:
		m = {}
		known = [set() for _ in xrange(10)]
		u5 = []
		u6 = []
		for clue in clues.split():
			c = ''.join(sorted(clue))
			if len(c) == 2:
				m[c] = '1'
				known[1] = set(c)
			elif len(c) == 3:
				m[c] = '7'
				known[7] = set(c)
			elif len(c) == 4:
				m[c] = '4'
				known[4] = set(c)
			elif len(c) == 7:
				m[c] = '8'
				known[8] = set(c)
			elif len(c) == 5:
				u5.append(c)
			else:
				u6.append(c)
		for c in u6:
			s = set(c)
			if s.issuperset(known[4]):
				m[c] = '9'
				known[9] = s
			elif s.issuperset(known[1]):
				m[c] = '0'
				known[0] = s
			else:
				m[c] = '6'
				known[6] = s
		for c in u5:
			s = set(c)
			if s.issuperset(known[1]):
				m[c] = '3'
				known[3] = s
			elif s.issubset(known[9]):
				m[c] = '5'
				known[5] = s
			else:
				m[c] = '2'
				known[2] = s
		out = int(''.join([m[''.join(sorted(i))] for i in outs.split()]))
		print out
		total += out
	return total


if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	t = part1(input_text)
	print "part1: %d" % (t,)
	t = part2(input_text)
	print "part2: %d" % (t,)
