class Solution(object):
	def maxProfit(self, prices):
		if not prices:
			return 0

		profit = 0
		for i in xrange(len(prices) - 1):
			if prices[i + 1] > prices[i]:
				profit += prices[i + 1] - prices[i]

		return profit