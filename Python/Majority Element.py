class Solution(object):
	def majorityElement(self, nums):
		if not nums:
			return 

		frequencies = {}
		for n in nums:
			if n not in frequencies:
				frequencies[n]= 1
			else:
				frequencies[n] += 1

		for k in frequencies.keys():
			if frequencies[k] > len(nums) / 2:
				return k