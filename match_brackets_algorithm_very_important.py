#the below code is for  multiple groupings or mixed pairs
def test_groupings(li, _map={'(': ')', '[': ']', '{': '}'}):
	stack = []
	for el in li:
		if el in _map:
			# opening element, add to stack to look for matching close
			stack.append(el)
		elif not stack or _map[stack[-1]] != el:
			# not an opening element; is the stack is empty?
			# or is this element not paired with the stack top?
			return False
		elif el == _map[stack[-1]]:
			stack.pop()
		else:
			# closing element matched, remove opening element from stack
			stack.pop()

	# if the stack is now empty, everything was matched
	return not stack

print test_groupings(['{', '[', '(', ')', ']', '}'])
#True
print test_groupings(['[', '(', ')', ']'])
#True
print test_groupings(['{', '[', '(', ']', ')', '}'])
#False
print test_groupings(['(', '{', '}', '[', ']', ')'])
#True
print "================================================================="
#the below solution is only for single dimension of nesting and not mixed pairs like above example inputs
def test_pairs(li, _map={'(': ')', '[': ']', '{': '}'}):
	l = len(li)
	if l % 2 == 1:
		# odd length list, can't be paired
		return False

	print li[:l//2]
	# pair up the first half with the second half, reversed
	for first, second in zip(li[:l // 2], reversed(li)):
		if _map.get(first) != second:
			# Either first is not a left bracket, or right bracket is not a match
			return False

	# everything tested, so everything matched
	return True

print test_pairs(['{', '[', '(', ')', ']', '}'])
#True
print test_pairs(['[', '(', ')', ']'])
#True
print test_pairs(['{', '[', '(', ']', ')', '}'])
#False
print "================================================================="
