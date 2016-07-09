class Solution(object):
	def combinationSum(self, candidates, target):
		if not candidates or not target:
			return []

		ret = []
		self.dfs(candidates, target, [], 0, ret)
		return ret

	def dfs(self, candidates, target, ans, start, ret):
		if sum(ans) == target and ans not in ret:
			ret.append(ans)

		for i in range(start, len(candidates)):
			if sum(ans) + candidates[i] <= target:
				self.dfs(candidates, target, ans + [candidates[i]], i, ret)

a = [2,3,6,7]
print Solution().combinationSum(a, 7)
