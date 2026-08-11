class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        ans, sol = [], []
        
        def findCombinations(ind):
            
            if ind == len(digits):
                ans.append("".join(sol))
                return
            
            for x in letters.get(digits[ind]):
                sol.append(x)
                findCombinations(ind+1)
                sol.pop()
        
        findCombinations(0)

        return ans