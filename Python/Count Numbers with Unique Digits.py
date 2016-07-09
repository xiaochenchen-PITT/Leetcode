class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		if n == 0:
			return 1

		dp = {}
		for i in range(1, n + 1):
			if i == 1:
				dp[i] = 10
			elif i == 2:
				dp[i] = dp[i - 1] + 9 * 9
				remainder = 9 * 9
			else:
				dp[i] = dp[i - 1] + remainder * (11 - i)
				remainder = remainder * (11 - i)
		if n > 10:
			return dp[10]
		return dp[n]

print Solution().countNumbersWithUniqueDigits(3)