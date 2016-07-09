class Solution(object):
	def bulbSwitch(self, n):
		# # brute force
		# if n < 3:
		# 	return n

		# bulbs = [-1 for i in range(n)] # -1 : off
		# for i in xrange(1, n + 1):
		# 	for j in range(0, n, i):
		# 		bulbs[j] = bulbs[j] * -1

		# ret = 0
		# for bulb in bulbs:
		# 	if bulb == 1:
		# 		ret += 1
		# return ret

		# math
		return int(math.sqrt(n))