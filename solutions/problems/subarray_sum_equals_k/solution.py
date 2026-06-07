class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mappings = {}
        mappings[0] = 1

        count = 0
        total = 0

        for element in nums:
            total += element 
            if (total - k) in mappings:
                count += mappings.get(total-k)

            if total not in mappings:
                mappings[total] = 1
            else:
                mappings[total] += 1

        return count
            
            