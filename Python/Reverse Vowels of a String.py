class Solution(object):
	def reverseVowels(self, s):
		if not s:
			return s
		
		l = 0
		r = len(s) - 1
		stringList = list(s)  # string concatenation makes Python slow
							  # use join() to pass on Leetcode 
		vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I', 'O', 'U']
		while l < r:
			while l < r and stringList[l] not in vowels:
				l += 1
			t = stringList[l]
			while l < r and stringList[r] not in vowels:
				r -= 1
			stringList[l], stringList[r] = stringList[r], stringList[l]
			l += 1
			r -= 1
		return "".join(stringList)
			
print Solution().reverseVowels("hello")