class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        sol, ans, ind = [], [], []

        def backtrack():

            if len(sol) == len(nums):
                ans.append(sol[:])
                return
            
            level = []
            for i in range(len(nums)):
                
                if len(level) > 0 and nums[i] == level[-1]:
                    continue

                if i not in ind:
                    ind.append(i)
                    sol.append(nums[i])
                    level.append(nums[i])
                    backtrack()
                    ind.pop()
                    ele = sol.pop()

        nums.sort()
        backtrack()
        return ans