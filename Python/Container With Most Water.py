class Solution(object):
	def maxArea(self, height):
		if not height:
			return -1

		ret = 0
		left = 0
		right = len(height) - 1
		while left <= right:
			ret = max(ret, min(height[left], height[right]) * (right - left))
			if height[left] < height[right]:
				left += 1
			else:
				right -= 1
		return ret