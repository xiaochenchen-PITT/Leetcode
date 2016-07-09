class Solution(object):
    def numTrees(self, n):
        dp = [1 for i in range(n + 1)]
        for i in xrange(1, n + 1):
        	if i == 1:
        		dp[i] = 1
        	elif i == 2:
        		dp[2] = 2
        	else:
        		count = 0
        		# can put 1,2,... nodes on left and i-1-1,i-1-2...nodes on right
        		for j in xrange(i): 
        			count += dp[j] * dp[i - 1 - j]
        		dp[i] = count
        return dp[n]

print Solution().numTrees(3)