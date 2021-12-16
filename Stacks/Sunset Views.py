def sunsetViews(buildings, direction):
    # Write your code here.
    num = len(buildings) - 1
	if direction == 'EAST':
		loop = range(num, -1, -1)
	else:
		loop = range(num + 1)
		
	stack = []
	height = 0
	for i in loop:
		if buildings[i] > height:
			stack.append(i)
			height = buildings[i]
	return stack if direction == 'WEST' else stack[::-1]
			
