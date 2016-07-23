class Solution(object):
	def findKthLargest(self, nums, k):
		if not nums:
			return -1
			
		queue = PriorityQueue()
		for n in nums:
			queue.add(n)
		return queue[k - 1]

class PriorityQueue():
	def __init__(self):
		self.q = []

	def __getitem__(self, k):
		return self.q[k]

	def add(self, n):
		for i in xrange(len(self.q)):
			if self.q[i] < n:
				self.q.insert(i, n)
				return
		self.q.append(n)

a = [3,2,1,5,4,6]
print Solution().findKthLargest(a, 2)
