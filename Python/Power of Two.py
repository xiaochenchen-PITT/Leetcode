class Solution(object):
	def isPowerOfTwo(self, n):
		if n <= 0:
			return False

		while n != 1:
			if n % 2 != 0:
				return False
			n /= 2
		return True

	def isPowerOfTwo2(self, n):
		# bit manipulation
		if n <= 0:
			return False

		bitCount = 0
		while n > 0:
			bitCount += n & 1
			n >>= 1
		return True	if bitCount == 1 else False