class Solution(object):
	def integerBreak(self, n):
		return max([self.splitInt(n, m) for m in range(2, n + 1)])

	def splitInt(self, n, m):
		multiplicator = n / m
		remainder = n % m
		return multiplicator ** (m - remainder) * (multiplicator + 1) ** remainder

print Solution().integerBreak(8)