class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        if sum(candies) < k:
            return 0

        i = 1
        j = max(candies)

        ans = -float('inf')

        def isPossible(val):
            count = 0
            for n in candies:
                count += (n//val)

            if count >= k:
                return True

            return False

        while i <= j:
            mid = (i+j) // 2
            if isPossible(mid):
                i = mid + 1
                ans = max(ans, mid)
            else:
                j = mid - 1

        return ans

            