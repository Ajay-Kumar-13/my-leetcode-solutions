class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        i = 1 
        j = x

        while i <= j:
            mid = (i + j) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                j = mid - 1
            else:
                i = mid + 1
                
        return j