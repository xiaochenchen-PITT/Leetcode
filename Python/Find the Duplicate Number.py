class Solution(object):
	def findDuplicate(self, nums):
		# O(NlogN) time, O(1) space
		if not nums:
			return -1

		left = 1
		right = len(nums) - 1
		while left <= right:
			middle = left + (right - left) / 2
			count = 0
			for n in nums:
				if n <= middle:
					count += 1
			if count <= middle:
				left = middle + 1
			else:
				right = middle - 1
		return left

m = [1,2,3,3,4,5]
m = [1,1,1,1,1,5]
# m = [1,2,2]
# m = [1,1,2]
# m = [1,1]
print Solution().findDuplicate(m)