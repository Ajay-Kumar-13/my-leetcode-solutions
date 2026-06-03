class Solution(object):

    def isHappy(self, n, sos=None):
        """
        :type n: int
        :rtype: bool
        """
        if (sos is None):
            sos = {}

        nums = list(str(n))
        sum = 0
        for ele in nums:
            sum += (int(ele) * int(ele))

        if (sum == 1):
            return True

        if n not in sos:
            sos[n] = sum
        
        if sum in sos:
            return False

        return self.isHappy(sum, sos)