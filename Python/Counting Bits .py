class Solution(object):
	def countBits(self, num):
		if num == 0:
			return [num]

		ret = []
		for n in range(num + 1):
			ret.append(self.countBits_helper(n))
		return ret

	def countBits_helper(self, n):
		if n == 0 or n == 1:
			return n

		return (n % 2) + self.countBits_helper(n / 2)

print Solution().countBits(5)