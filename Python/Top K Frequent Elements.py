class Solution(object):
	def topKFrequent(self, nums, k):
		# Your algorithm's time complexity must be better than O(n log n), 
		# where n is the array's size.
		if not nums:
			return []

		frequencies = {}
		ret = [None for i in range(k)]

		for n in nums:
			if n not in frequencies:
				frequencies[n] = 1
			else:
				frequencies[n] += 1
		print frequencies

		for key in frequencies.keys():
			# binary search
			l = 0
			r = len(ret) - 1
			while l <= r:
				m = (l + r) / 2
				if ret[m] == None or frequencies[key] > frequencies[ret[m]]:
					r = m - 1
				else:
					l = m + 1
			if l < len(ret):
				ret[l + 1:] = ret[l:-1]
				ret[l] = key
		return ret

print Solution().topKFrequent([3,0,1,0], 1)