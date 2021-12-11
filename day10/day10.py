import sys
import os
import re

test_text = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''


def part1(text):
	scores = {')':3,']':57,'}':1197,'>':25137}
	expected = {')':'(', ']':'[','}':'{','>':'<'}
	total = 0
	for l in text.splitlines():
		stack = []
		for c in l:
			if c in ['(','[','{','<']:
				stack.append(c)
			else:
				if expected[c] == stack[-1]: #len(stack) and 
					stack.pop()
				else:
					total += scores[c]
					break
	return total

def part2(text):
	scores = {')':1, ']':2, '}':3, '>':4}
	expected = {')':'(', ']':'[','}':'{','>':'<'}
	expected.update(dict([(v,k) for k,v in expected.iteritems()]))
	totals =  []
	for l in text.splitlines():
		stack = []
		invalid = False
		total = 0
		for c in l:
			if c in ['(','[','{','<']:
				stack.append(c)
			else:
				if expected[c] == stack[-1]:
					stack.pop()
				else:
					invalid = True
					break
		if not invalid:
			stack.reverse()
			for c in stack:
				total *= 5
				total += scores[expected[c]]
			totals.append(total)
	totals.sort()
	return totals[len(totals)/2]

if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] == 'test':
		input_text = test_text
	else:
		fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
		with open(fname, 'rb') as f:
			input_text = f.read()
	
	c = part1(input_text)
	print "part1: ", c
	c = part2(input_text)
	print "part2: ", c

