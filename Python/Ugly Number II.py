class Solution(object):
	def nthUglyNumber(self, n):
		if n <= 0:
			return -1

		index2, index3, index5 = 0, 0, 0
		uglys = [1]
		while len(uglys) < n:
			ugly2, ugly3, ugly5 = uglys[index2] * 2, uglys[index3] * 3, uglys[index5] * 5
			ugly = min(ugly2, ugly3, ugly5)
			if ugly == ugly2:
				index2 += 1
			if ugly == ugly3:
				index3 += 1
			if ugly == ugly5:
				index5 += 1
			if ugly not in uglys:
				uglys.append(ugly)
		return uglys[n - 1]

print Solution().nthUglyNumber(10)