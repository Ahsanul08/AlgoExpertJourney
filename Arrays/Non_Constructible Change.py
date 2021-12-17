def nonConstructibleChange(coins):
    # Write your code here.
	coins.sort()
	summed = 0
	for coin in coins:
		if coin > summed +1:
			return summed + 1
		summed += coin
	return summed + 1
		
