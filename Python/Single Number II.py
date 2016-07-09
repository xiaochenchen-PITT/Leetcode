class Solution(object):
	def singleNumber(self, nums):
		counts = [0 for i in range(32)]
		ret = 0
		for i in range(32):
			for n in nums:
				if ((n >> i) & 1) == 1:
					counts[i] +=1
			ret |= ((counts[i] % 3) << i)
		return ret

a= [3,3,3,1]
print Solution().singleNumber(a)