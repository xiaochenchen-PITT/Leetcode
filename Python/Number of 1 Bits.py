class Solution(object):
	def hammingWeight(self, n):
		bitCount = 0
		while n > 0:
			bitCount += n & 1
			n >>= 1
		return bitCount

print Solution().hammingWeight(11)