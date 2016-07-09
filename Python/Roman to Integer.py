class Solution(object):
	def romanToInt(self, s):
		if not s:
			return 0

		romans = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

		ret = romans[s[-1]]
		for i in xrange(len(s) - 2, -1, -1):
			if romans[s[i]] >= romans[s[i + 1]]:
				ret += romans[s[i]]
			else:
				ret -= romans[s[i]]
		return ret