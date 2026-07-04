class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def isPossible(nums, mid, k):
            
            prefix = 0
            for n in nums:
                prefix += n
                if prefix > mid:
                    prefix = n
                    k -= 1
                    
            if k >= 1:
                return True
                
            return False
        
        i =  max(nums)
        j = sum(nums)
        
        minimizedMaximum = float('inf')
        
        while i <= j:
            mid = (i+j) // 2
            
            if isPossible(nums, mid, k):
                minimizedMaximum = min(minimizedMaximum, mid)
                j = mid - 1
            else:
                i = mid + 1
                
        return minimizedMaximum