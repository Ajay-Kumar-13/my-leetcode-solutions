class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        answer = 0

        pairs  = 0
        frequency = {}
        i = 0
        for j in range(len(nums)):
            freq = frequency.get(nums[j], 0) 
            if freq + 1 >= 2:
                pairs += freq

            frequency[nums[j]] = frequency.get(nums[j], 0) + 1

            freq = frequency.get(nums[j], 0) 
            while pairs >= k:
                answer += (len(nums) - j)
               
                freq = frequency.get(nums[i])
                
                pairs -= (freq - 1)
                frequency[nums[i]] = freq - 1

                i += 1
                

        return answer