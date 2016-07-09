class Solution(object):
    def addDigits(self, num):
        if 0 <= num < 10:
            return num

        while num > 9:
            n = num % 10
            num = num / 10
            num = n + num
        return num

    # Follow up:Could you do it without any loop/recursion in O(1) runtime? 
    # hint : What are all the possible results? is it periodical?
    def addDigits_followUp(self, num):
        if num == 0:
            return 0

        res = [1,2,3,4,5,6,7,8,9]
        return res[num % 9 - 1]

print Solution().addDigits_followUp(39)
