class Solution(object):
	def titleToNumber(self, s):
		if not s:
			return -1

		ret = 0
		alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		for i in xrange(len(s) - 1, -1, -1):
			ret += (alf.index(s[i]) + 1) * 26 ** (len(s) - 1 - i)
		return ret

print Solution().titleToNumber("AB")