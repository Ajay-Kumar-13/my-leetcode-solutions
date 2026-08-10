class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def getAllSubsets(ind, current, ans):

            if ind == len(nums):
                return 

            current.append(nums[ind])

            ans.append(current[:])
            getAllSubsets(ind+1, current, ans)

            ele = current.pop()
            while ind+1 < len(nums) and ele == nums[ind+1]:
                ind += 1

            getAllSubsets(ind+1, current, ans)

            return ans

        nums.sort()
            
        return getAllSubsets(0, [], [[]])

