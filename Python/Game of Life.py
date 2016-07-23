class Solution(object):
	def gameOfLife(self, board):
		# in- place
		if not board or not board[0]:
			return

		for i in xrange(len(board)):
			for j in range(len(board[0])):
				liveNeighbor = self.getLiveneighbor(i, j, board)
				if board[i][j] == 1:
					if liveNeighbor == 2 or liveNeighbor == 3:
						board[i][j] = 3
				else:
					if liveNeighbor == 3:
						board[i][j] = 2

		for i in xrange(len(board)):
			for j in xrange(len(board[0])):
				board[i][j] = (board[i][j] & 2) >> 1
		return board

	def getLiveneighbor(self, i, j, board):
		cnt = 0
		d = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
		for dx, dy in d:
			x = dx + j
			y = dy + i
			if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
				continue
			else:
				if board[y][x] & 1 == 1:
					cnt += 1
		return cnt

b = [[1,1], [1, 0]]
print Solution().gameOfLife(b)