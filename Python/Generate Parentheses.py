class Solution(object):
	def generateParenthesis(self, n):
		if not n:
			return []

		ret = []
		self.dfs(n, 0, 0, "", ret)
		return ret

	def dfs(self, n, left, right, ans, ret):
		if left == n:
			while right < n:
				ans += ")"
				right += 1
			ret.append(ans)
			return

		for c in ["(", ")"]:
			if c == "(":
				self.dfs(n, left + 1, right, ans + c, ret)
			else:
				if right >= left:
					continue
				else:
					self.dfs(n, left, right + 1, ans + c, ret)

print Solution().generateParenthesis(4)