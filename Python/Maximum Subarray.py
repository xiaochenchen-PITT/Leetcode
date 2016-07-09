class Solution(object):
	def maxSubArray(self, nums):
		max_ending_here = max_so_far = nums[0]
		for x in nums[1:]:
			max_ending_here = max(x, max_ending_here + x)
			max_so_far = max(max_so_far, max_ending_here)
		return max_so_far

a = [-2]
print Solution().maxSubArray(a)