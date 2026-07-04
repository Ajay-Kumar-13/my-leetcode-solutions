class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def isPossible(nums, mid, k):
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    k -= 1
                    i += 2
                else:
                    i += 1
                    
            if k <= 0:
                return True
                
            return False
        
        i = min(nums)
        j = max(nums)
        
        minCapability = float('inf')
        
        while i <= j:
            mid = (i + j) // 2
            
            if isPossible(nums, mid, k):
                minCapability = min(minCapability, mid)
                j = mid - 1
            else:
                i = mid + 1
                
        return minCapability