class Solution(object):
	def maxProfit(self, prices):
		if not prices:
			return 0

		minPrice = prices[0]
		maxProfit = 0
		for i in xrange(len(prices)):
			minPrice = min(minPrice, prices[i])
			maxProfit = max(maxProfit, prices[i] - minPrice)
		return maxProfit