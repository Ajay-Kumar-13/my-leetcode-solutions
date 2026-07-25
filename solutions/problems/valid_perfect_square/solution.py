class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        i = 1
        j = num

        while i <= j:
            mid = (i+j)//2

            n = mid*mid

            if n == num:
                return True
            elif n > num:
                j = mid - 1
            else:
                i = mid + 1

        return False