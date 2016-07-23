class Solution(object):
	def searchMatrix(self, matrix, target):
		# divide and conquer
		if not matrix:
			return False
		print matrix

		if len(matrix) <= 2 and len(matrix[0]) <= 2:
			for i in xrange(len(matrix)):
				for j in xrange(len(matrix[0])):
					if matrix[i][j] == target:
						return True
			return False

		middle = ((len(matrix) - 1) / 2, (len(matrix[0]) - 1) / 2)
		print matrix[middle[0]][middle[1]]
		if matrix[middle[0]][middle[1]] == target:
			return True
		elif matrix[middle[0]][middle[1]] < target:
			return (self.searchMatrix(self.cutMatrix(matrix, middle[1], len(matrix[0]) - 1, 0, middle[0]), target) 
			or self.searchMatrix(self.cutMatrix(matrix, 0, middle[1], middle[0], len(matrix) - 1), target) 
			or self.searchMatrix(self.cutMatrix(matrix, middle[1], len(matrix[0]) -1, middle[0], len(matrix) - 1), target)
			)
		else:
			return (self.searchMatrix(self.cutMatrix(matrix, middle[1], len(matrix[0]) - 1, 0, middle[0]), target) 
			or self.searchMatrix(self.cutMatrix(matrix, 0, middle[1], middle[0], len(matrix) - 1), target) 
			or self.searchMatrix(self.cutMatrix(matrix, 0, middle[1], 0, middle[0]), target)
			)

	def cutMatrix(self, matrix, xStart, xEnd, yStart, yEnd):
		smallMatrix = []
		for i in range(len(matrix)):
			if i >= yStart and i <= yEnd:
				smallMatrix.append(matrix[i][xStart : xEnd + 1])
		return smallMatrix

	def searchMatrix2(self, matrix, target):
		# O(m * lgN)
		if not matrix:
			return False

		for y in range(len(matrix)):
			if self.binarySearch(matrix[y], target):
				return True
		return False

	def binarySearch(self, l, target):
		if not l:
			return False

		left = 0
		right = len(l) - 1
		while left <= right:
			middle = left + (right - left) / 2
			if l[middle] == target:
				return True
			elif l[middle] < target:
				left = middle + 1
			else:
				right = middle - 1
		return False

m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
m = [[1],[2],[3],[4],[5]]
m = [
	[ 1, 2, 3, 4, 5],
	[ 6, 7, 8, 9,10],
	[11,12,13,14,15],
	[16,17,18,19,20],
	[21,22,23,24,25]
]
print Solution().searchMatrix2(m, 5)