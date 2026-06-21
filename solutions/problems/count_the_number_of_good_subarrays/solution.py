class Solution(object):
    
    def possible_combinations(self, n, r):
        if n < r:
            return 0
            
        if n == r:
            return 1
            
        num = 1
        den = 1
        
        for i in range(r):
            num *= (n-i)
            den *= i+1
            
        return num//den
    
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        frequency = {}
        
        i = 0
        j = 0
        r = 2
        length = len(nums)
        
        total_pairs = 0
        good_sub_arrays = 0
        
        while j < length:
            if total_pairs < k:
                val = nums[j]
                frequency[val] = frequency.get(val, 0) + 1
                n = frequency.get(val)
                if n > 1:
                    total_pairs += (self.possible_combinations(n, r) - self.possible_combinations(n-1, r))
                j += 1
            else:
                # print(nums[i:j])
                good_sub_arrays += 1 + length - j
                val = nums[i]
                n = frequency.get(val)
                if n > 1:
                    total_pairs -= (self.possible_combinations(n, r) - self.possible_combinations(n-1, r))
                frequency[val] = frequency.get(val, 0) - 1
                i += 1
        
        while total_pairs >= k:
            print(nums[i:j])
            good_sub_arrays += 1 + length - j
            val = nums[i]
            n = frequency.get(val)
            if n > 1:
                total_pairs -= (self.possible_combinations(n, r) - self.possible_combinations(n-1, r))
            frequency[val] = frequency.get(val, 0) - 1
            i += 1

        return good_sub_arrays