class Solution(object):
	def rotate(self, matrix):
		if not matrix:
			return

		n = len(matrix)
		for i in xrange(n):
			for j in range(n - i):
				matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]
		print matrix

		for i in xrange(n / 2):
				matrix[i], matrix[n  - 1 - i] = matrix[n  - 1 - i], matrix[i]
		# return matrix


m = [[1, 2, 3, 4], 
	 [5, 6, 7, 8],
	 [9,10,11,12],
	[13,14,15,16]]
print Solution().rotate(m)