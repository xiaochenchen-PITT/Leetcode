class Solution(object):
	def permute(self, nums):
		if not nums:
			return []

		ret = []
		self.permute_helper(nums, ret, [])
		return ret

	def permute_helper(self, nums, ret, ans):
		# exit point of dfs
		if len(ans) == len(nums):
			ret.append(ans)
			return 

		for i in range(len(nums)):
			if nums[i] not in ans:
				self.permute_helper(nums, ret, ans + [nums[i]])

m = [1,2,3]
print Solution().permute(m)