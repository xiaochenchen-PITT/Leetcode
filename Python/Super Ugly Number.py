class Solution(object):
	def nthSuperUglyNumber(self, n, primes):
		if n == 0:
			return -1

		if not primes:
			return -1

		ugly = 1
		count = 1
		primesMultiples = primes
		while count < n:
			for i in xrange(len(primes)):
				pass
		return ugly

