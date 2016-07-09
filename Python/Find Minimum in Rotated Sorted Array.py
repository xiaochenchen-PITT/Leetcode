class Solution(object):
	def findMin(self, nums):
		if not nums:
			return -1

		left = 0
		right = len(nums) - 1
		while left <= right:
			if left == right:
				return nums[left]

			middle = (left + right) / 2
			if nums[middle] < nums[right]:
				right = middle
			else:
				left = middle + 1
		return nums[left]

a = [4,5,6,7,0,1,2]
a = [3]
print Solution().findMin(a)



