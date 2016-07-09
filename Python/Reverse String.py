class Solution(object):
	def reverseString(self, s):
		if not s:
			return s

		l = 0
		r = len(s) - 1
		stringList = list(s)  # string concatenation makes Python slow
							  # use pyhtonic list swap and join() to pass on Leetcode 
		while l < r:
			t = stringList[l]
			stringList[l], stringList[r] = stringList[r], stringList[l]
			l += 1
			r -= 1
		return "".join(stringList)

print Solution().reverseString("heelo")