class Solution(object):
	def rob(self, nums):
		if not nums:
			return 0

		dp = [0 for i in range(len(nums))]
		for i in range(len(nums)):
			if i == 0:
				dp[i] = nums[i]
			elif i == 1:
				dp[i] = max(nums[0], nums[1])
			else:
				dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
		return dp[len(nums) - 1]

a = [1,1,2,1]
print Solution().rob(a)