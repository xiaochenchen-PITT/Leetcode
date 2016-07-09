# coding: utf-8
class Solution(object):
	def maxProduct(self, words):
		# brute force
		if not words:
			return 0

		ret = 0
		for i in range(len(words)):
			for j in range(i + 1, len(words)):
				if self.shareCommonLetter(words[i], words[j]):
					ret = max(ret, len(words[i]) * len(words[j]))
		return ret

	def shareCommonLetter(self, a, b):
		for c in a:
			if c in b:
				return False
		return True

	def maxProduct2(self, words):
		"""
		其实因为全部都是小写的字母，用int 就可以存储每一位的信息
		"""
		n = len(words)
		elements = [0] * n
		for i, s in enumerate(words):
			for c in s:
				elements[i] |= 1 << (ord(c) - ord('a')) # 1左移若干位

		ans = 0
		for i in xrange(n):
			for j in xrange(i + 1, n):
				if not (elements[i] & elements[j]):
					ans = max(ans, len(words[i]) * len(words[j]))
		return ans
		


words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print Solution().maxProduct(words)