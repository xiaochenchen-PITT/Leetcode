class Solution(object):
	def rob(self, nums):
		if not nums:
			return 0

		robFirst = [0 for i in range(len(nums))]
		for i in range(len(nums)):
			if i == 0:
				robFirst[i] = nums[i]
			elif i == 1:
				robFirst[i] = robFirst[i - 1]
			else:
				if i == len(nums) - 1:
					robFirst[i] = robFirst[i - 1]
				else:
					robFirst[i] = max(robFirst[i - 2] + nums[i], robFirst[i - 1])

		robNoFirst = [0 for i in range(len(nums))]
		for i in xrange(len(nums)):
			if i == 0:
				robNoFirst[i] = 0
			elif i == 1:
				robNoFirst[i] = nums[i]
			else:
				robNoFirst[i] = max(robNoFirst[i - 2] + nums[i], robNoFirst[i - 1])

		return max(robFirst[len(nums) - 1], robNoFirst[len(nums) - 1])

a = [1,1,1]
print Solution().rob(a)