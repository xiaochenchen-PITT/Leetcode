class Solution(object):
	def isHappy(self, n):
		if n <= 0:
			return False

		duplicates = []
		while n != 1:
			duplicates.append(n)
			s = 0
			while n > 0:
				s += (n % 10) ** 2
				n /= 10
			n = s
			if n in duplicates:
				return False
		return True
				