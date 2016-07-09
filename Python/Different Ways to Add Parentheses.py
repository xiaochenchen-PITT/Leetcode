class Solution(object):
	def diffWaysToCompute(self, input):
		if not input:
			return []

		ret = []	
		for i in range(len(input)):
			if input[i] == '+' or input[i] == '-' or input[i] == '*':
				left = self.diffWaysToCompute(input[:i])
				right = self.diffWaysToCompute(input[i + 1:])
				for n in left:
					for m  in right:
						if input[i] == '+':
							ret.append(n + m)
						elif input[i] == '-':
							ret.append(n - m)
						else:
							ret.append(n * m)
		if not ret:
			ret.append(int(input))
		return ret

print Solution().diffWaysToCompute("2*3-4*5")
