class Solution(object):
	def moveZeroes(self, nums):
		if not nums:
			return

		lastZero = len(nums)- 1
		index = len(nums) - 1
		while index >= 0:
			if nums[index] == 0:
				move = index
				while move < len(nums) - 1:
					t = nums[move + 1]
					nums[move + 1] = nums[move]
					nums[move] = t
					move += 1
			index -= 1
		return nums

print Solution().moveZeroes([0, 1, 0, 3, 12])
