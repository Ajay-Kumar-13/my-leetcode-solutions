# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i = 1 
        j = n

        while i <= j:
            mid = (i + j) // 2
            isNumber = guess(mid)
            if isNumber == 0:
                return mid
            elif isNumber == -1:
                j = mid - 1
            elif isNumber == 1:
                i = mid + 1