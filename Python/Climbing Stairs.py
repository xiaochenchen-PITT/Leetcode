class Solution(object):
	def climbStairs(self, n):
		if n == 1 or n == 2:
			return n

		dp = [0 for i in range(n + 1)]
		for i in xrange(1, n + 1):
			if i == 1:
				dp[i] = 1
			elif i == 2:
				dp[i] = 2
			else:
				dp[i] = dp[i - 1] + dp[i - 2]
		return dp[n]