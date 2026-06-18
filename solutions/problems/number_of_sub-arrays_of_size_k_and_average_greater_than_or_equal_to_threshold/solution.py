class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count = 0

        s = 0
        for x in range(k):
            s += arr[x]
        
        if s//k >= threshold:
            count += 1
        
        i = 0
        for x in range(k, len(arr)):
            i += 1
            s -= arr[i-1]
            s += arr[x]
            if s // k >= threshold:
                count += 1

        return count