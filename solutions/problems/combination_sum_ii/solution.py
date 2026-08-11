class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans, sol = [], []

        def findCombinations(ind, total):

            if total == 0:
                ans.append(sol[:])
                return

            if total < 0 or total > target or ind == len(candidates):
                return
            
            sol.append(candidates[ind])
            findCombinations(ind+1, total - candidates[ind])
            
            n = sol.pop()

            while ind < len(candidates)-1 and n == candidates[ind+1]:
                ind += 1

            findCombinations(ind+1, total)
            

        candidates.sort()
        findCombinations(0, target)
        return ans