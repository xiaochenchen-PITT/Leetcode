class Solution(object):
	def intersection(self, nums1, nums2):
		if not nums1 or not nums2:
			return []

		ret = []
		for n in nums1:
			if n in nums2 and n not in ret:
				ret.append(n)

		return ret
