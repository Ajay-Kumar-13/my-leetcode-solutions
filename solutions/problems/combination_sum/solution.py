class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans, sol = [], []
    
        def findCombination(ind, total):
            
            if total == 0:
                ans.append(sol[:])
                return
            
            if total < 0 or total > target or ind == len(candidates):
                return
            
            sol.append(candidates[ind])
            findCombination(ind, total-candidates[ind])
            
            sol.pop()
            
            findCombination(ind+1, total)
        
        candidates.sort()
        findCombination(0, target)
        return ans