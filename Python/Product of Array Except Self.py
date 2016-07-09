class Solution(object):
	# def productExceptSelf_failed(self, nums):
	# 	# with division,  failed when there is zero in the array
	# 	product = 1
	# 	for n in nums:
	# 		product *= n

	# 	output = []
	# 	for n in nums:
	# 		output.append(product / n)
	# 	return output

	def productExceptSelf(self, nums):
		# without division and in O(n)
		# hint : output[i] = product of the numbers before i *
							# product of the numbers after i 

		products_forward = [1]
		for i in xrange(len(nums)):
			products_forward.append(products_forward[-1] * nums[i])

		products_backward = [1]
		for i in xrange(len(nums)):
			products_backward.append(products_backward[-1] * nums[len(nums) - 1 - i])
		products_backward = products_backward[::-1]

		output = []
		for i in xrange(len(nums)):
			output.append(products_forward[i] * products_backward[i + 1])
		return output

	def productExceptSelf_followup(self, nums):
		# constant space
		output = []
		p = 1 # use p as products_forward
		for i in xrange(len(nums)):
			p *= nums[len(nums) - 1 - i]
			output.append(p) # use output as products_backward
		output = output[::-1]
		output.append(1)
		# print output

		p = 1
		for i in range(len(nums)):
			output[i] = p * output[i + 1]
			p *= nums[i]
		return output[:-1]

print Solution().productExceptSelf_followup([1,2,3,4])



