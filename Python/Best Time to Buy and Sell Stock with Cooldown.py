#!/usr/bin/env python 
#!encoding: utf-8

class Solution(object):
	def maxProfit(self, prices):
		if not prices:
			return 0

		# sells[i]表示在第i天不持有股票所能获得的最大累计收益
		sells = [0 for i in range(len(prices))]
		# buys[i]表示在第i天持有股票所能获得的最大累计收益
		buys =[0 for i in range(len(prices))]
		for i in xrange(len(prices)):
			if i == 0:
				sells[i] = 0
				buys[i] = -prices[i]
			elif i == 1:
				sells[i] = max(sells[i - 1], prices[i] - prices[i - 1])
				buys[i] = max(buys[i - 1], -prices[i])
			else:
				sells[i] = max(sells[i - 1], buys[i - 1] + prices[i])
				buys[i] = max(buys[i - 1], sells[i - 2] - prices[i])
		return sells[len(prices) - 1]