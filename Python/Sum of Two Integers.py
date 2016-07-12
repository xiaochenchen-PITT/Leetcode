class Solution(object):
	# def getSum(self, a, b):
		# """This does not work for Python. Because:
		# Python doesnot use 8-bit numbers.
		# I USED to use however many bits were native to your machine,
		# but since it was non-portable,
		# it recently switched to using an INFINITE numbers of bits.
		# Thus the number -5 is treated as 
		# '...1111111111111111111111011'
		# """
	# 	ans = 0
	# 	carry = 0
	# 	i = 0
	# 	while i < 32:
	# 		lower_a = a & 1
	# 		lower_b = b & 1
	# 		ans |= (lower_a ^ lower_b ^ carry) << i
	# 		carry = (lower_a & lower_b) | (lower_a & carry) | (lower_b & carry)
	# 		i += 1
	# 		a = a >> 1
	# 		b = b >> 1
	# 	return ans

	def getSum(self, a, b):
		MOD     = 0xFFFFFFFF
		MAX_INT = 0x7FFFFFFF
		while b != 0:
			a, b = (a ^ b) & MOD, ((a & b) << 1) & MOD
		return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT

print Solution().getSum(-3, 2)