class Solution(object):
	def searchInsert(self, nums, target):
		if not nums:
			return -1

		left = 0
		right = len(nums) - 1
		while left <= right:
			middle = left + (right - left) / 2	
			if nums[middle] == target:
				return middle
			elif nums[middle] < target:
				left = middle + 1
			else:
				right = middle - 1
		return left

a = [1,3,5,6]
print Solution().searchInsert(a, 3)