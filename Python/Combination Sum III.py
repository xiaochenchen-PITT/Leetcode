class Solution(object):
	def combinationSum3(self, k, n):
		if k <= 0 or n <= 0:
			return []

		ret = []
		self.dfs(k, n, [], 1, ret)
		return ret

	def dfs(self, k, n, ans, start, ret):
		if len(ans) == k and sum(ans) == n:
			if ans not in ret:
				ret.append(ans)

		for i in xrange(start, 10):
			if len(ans) < k and sum(ans) + i <= n and i not in ans:
				self.dfs(k, n, ans + [i], i + 1, ret)

print Solution().combinationSum3(3, 7)

