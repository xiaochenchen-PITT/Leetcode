class Solution(object):
	def permuteUnique(self, nums):
		if not nums:
			return []

		ret = []
		nums.sort()
		self.permuteUnique_helper(nums, [], ret, [])
		return ret

	def permuteUnique_helper(self, nums, visited, ret, ans):
		if len(ans) == len(nums) and ans not in ret:
			ret.append(ans)
			return 

		for i in range(len(nums)):
			if i in visited or (i != 0 and nums[i] == nums[i - 1] and i - 1 in visited):
				continue
			self.permuteUnique_helper(nums, visited + [i], ret, ans + [nums[i]])

m = [1,1,0,0,1,-1,-1,1]
print Solution().permuteUnique(m)