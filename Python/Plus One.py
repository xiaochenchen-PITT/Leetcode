class Solution(object):
	def plusOne(self, digits):
		digit = len(digits) - 1
		while digit >= 0 and digits[digit] + 1 == 10:
			digits[digit] = 0
			digit -= 1
		if digit == -1:
			digits = [1] + digits
		else:
			digits[digit] = digits[digit] + 1
		return digits

d = [9,9,9]
print Solution().plusOne(d)