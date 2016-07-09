class Solution(object):
	def canWinNim(self, n):
		if 0 <= n <= 3:
			return True
		elif n == 4:
			return False
		elif 5 <= n <= 7:
			return True
		else:
			return self.canWinNim(n - 4)

	def canWinNim2(self, n):
		for x in range(1, 4):
			if (n - x) % 4 == 0:
				return True
		return False

s = Solution()
for i in range(1, 100):
	assert s.canWinNim(i) == s.canWinNim2(i)