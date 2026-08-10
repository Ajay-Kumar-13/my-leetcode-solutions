class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def getAllSubsets(ind, current, ans):
        
            if ind == len(nums):
                return 

            
            current.append(nums[ind])
            
            ans.append(current[:])
            
            getAllSubsets(ind+1, current, ans)

            current.pop()            
            getAllSubsets(ind+1, current, ans)
            
            return ans
            
        return getAllSubsets(0, [], [[]])
    