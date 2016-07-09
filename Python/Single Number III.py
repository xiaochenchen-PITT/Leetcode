class Solution(object):
	# linear runtime complexity and constant space complexity?
	def singleNumber(self, nums):
		if not nums:
			return []

		#O(n) time and O(n) space
		# dup = []
		# ret = []
		# for n in nums:
		# 	if n in dup:
		# 		if n in ret:
		# 			ret.remove(n)
		# 	else:
		# 		dup.append(n)
		# 		ret.append(n)
		# return ret

		#O(n) time and O(1) space
		xor = 0
		for n in nums:
			xor ^= n

		# find the least significant 1 bit
		#k = (xor & (xor - 1)) ^ xor # Amazing!
		k = 1
		while (xor % 2 != 1):
			xor /= 2
			k *= 2

		a = 0
		b = 0
		for n in nums:
			if (n & k) == 0:
				a ^= n
			else:
				b ^= n
		return [a, b]



print Solution().singleNumber([1, 2, 1, 3, 2, 5])