def balancedBrackets(string):
    # Write your code here.
	stack = []
	opening = '([{'
	closing = '}])'
	mapper = {'}': '{', ')': '(', ']': '['}
	for i in string:
		if i in opening:
			stack.append(i)
		elif i in closing:
			if stack == []:
				return False
			if stack[-1] == mapper.get(i):
				stack.pop()
			else:
				return False
	return len(stack) == 0
