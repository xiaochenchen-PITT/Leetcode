class Solution(object):
	def uniquePaths(self, m, n):
		if m * n == 0:
			return 0

		dp = [[0 for j in range(n)] for i in range(m)]
		for i in xrange(m):
			for j in xrange(n):
				if i == 0:
					dp[i][j] = 1
				elif j == 0:
					dp[i][j] = 1
				else:
					dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		return dp[m - 1][n - 1]

print Solution().uniquePaths(2,1)