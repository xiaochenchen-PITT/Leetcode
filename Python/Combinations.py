class Solution(object):
	def combine(self, n, k):
		if n * k == 0:
			return []

		ret = []
		self.dfs(n, k, [], 1, ret)
		return ret

	def dfs(self, n, k, ans, start, ret):
		# if TLE, then terminate it early
		# If the remaining candidates are not enough to fill in the combnations
		if n - start + 1 < k - len(ans):
			return

		if len(ans) == k:
			ret.append(ans)
			return

		for i in xrange(start, n + 1):
			self.dfs(n, k, ans + [i], i + 1, ret)

print Solution().combine(20, 16)