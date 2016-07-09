#!/usr/bin/env python
#coding=utf-8

class Solution(object):
	def grayCode(self, n):
		# n = 0: 0
		# n = 1: 0, 1
		# n = 2: 00, 01, 11, 10  (0, 1, 3, 2)
		# n = 3: 000, 001, 011, 010, 110, 111, 101, 100 (0, 1, 3, 2, 6, 7, 5, 4)
		# 以n = 3为例，grey code中前4个包括了n = 2的所有gray code。后4个则是前4个逆序后加上2^2。
		# 推广：n = i的grey code的前一半包括了n = i-1的所有grey code，而后一半则为前一半逆序后加上2^(i-1)。
		if n == 0:
			return [0]
		
		firstHalf = self.grayCode(n - 1)
		ret = firstHalf
		for i in reversed(firstHalf):
			ret.append((1 << (n - 1)) | i)
		return ret

print Solution().grayCode(2)