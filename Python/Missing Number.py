class Solution(object):
	def missingNumber(self, nums):
		sum = 0
		for i in range(len(nums) + 1):
			sum += i
		for n in nums:
			sum -= n
		return sum
			
		