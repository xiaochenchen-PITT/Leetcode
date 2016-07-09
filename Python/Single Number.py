class Solution(object):
	def singleNumber(self, nums):
		ret = 0
		for n in nums:
			ret = ret ^ n
		return ret

arr = [1,2,234,2,34,34,1]
print Solution().singleNumber(arr)