class Solution(object):
	def removeElement(self, nums, val):
		if not nums:
			return 0

		removeIndex = len(nums) - 1
		i = 0
		while i < removeIndex:
			while i < removeIndex and nums[i] != val:
				i += 1
			nums[i], nums[removeIndex] = nums[removeIndex], nums[i]
			removeIndex -= 1

		for i in xrange(len(nums)):
			if nums[i] == val:
				return i

a = [3,3,3]
print Solution().removeElement(a, 3)