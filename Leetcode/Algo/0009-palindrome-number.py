class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reservedNum = 0
        temp = x
        while temp > 0:
            reservedNum = reservedNum * 10 + temp % 10
            temp/=10
        return x == reservedNum
        