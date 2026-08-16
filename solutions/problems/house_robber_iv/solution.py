class Solution:
    def minCapability(self, nums, k):
        
        i = min(nums)
        j = max(nums)

        def possible(val):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= val:
                    count += 1
                    i += 2
                    continue
                i += 1

            if count >= k:
                return True

            return False
        
        ans = float('inf')
        while i <= j:
            mid = (i+j) // 2
            if possible(mid):
                ans = min(ans, mid)
                j = mid - 1
            else:
                i = mid + 1

        return ans