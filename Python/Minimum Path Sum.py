class Solution(object):
	def minPathSum(self, grid):
		if not grid:
			return -1

		m = len(grid[0])
		n = len(grid)
		dp = [[0 for x in range(m)] for y in range(n)]

		for i in xrange(n):
			for j in xrange(m):
				if i == 0:
					dp[i][j] = sum([grid[0][x] for x in range(j + 1)])
				elif j == 0:
					dp[i][j] = sum([grid[y][0] for y in range(i + 1)])
				else:
					dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
		return dp[n - 1][m - 1]