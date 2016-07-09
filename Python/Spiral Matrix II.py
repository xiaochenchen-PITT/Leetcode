class Solution(object):
	def generateMatrix(self, n):
		if n  <= 0:
			return []

		ret = [[0 for x in range(n)] for y in range(n)]
		x, y = 0, 0
		up, down,left, right = 0, 0, 0, 1
		i = 1
		while i <= n ** 2:
			ret[y][x] = i
			if right:
				x += 1
				if x == n or ret[y][x] != 0: # change direction
					x -= 1
					y += 1
					right = 0
					down = 1
			elif down:
				y += 1
				if y == n or ret[y][x] != 0:
					y -= 1
					x -= 1
					down = 0
					left = 1
			elif left:
				x -= 1
				if x < 0 or ret[y][x] != 0:
					x += 1
					y -= 1
					left = 0
					up = 1
			else:
				y -= 1
				if y < 0 or ret[y][x] != 0:
					y += 1
					x += 1
					up = 0
					right = 1
			i += 1
		return ret

print Solution().generateMatrix(4)