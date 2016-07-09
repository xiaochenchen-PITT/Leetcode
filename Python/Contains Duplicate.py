class Solution(object):
	def containsDuplicate(self, nums):
		if not nums:
			return False

		nums.sort()
		for i in xrange(len(nums) - 1):
			if nums[i] == nums[i + 1]:
				return True

		return False

print Solution().containsDuplicate([1,12])