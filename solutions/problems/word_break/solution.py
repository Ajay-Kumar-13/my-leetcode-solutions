class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        l = len(s)

        dp = []

        current_string = ""

        for i in range(l):
            current_string += s[i]
            j = i-1
            
            found = False

            while len(dp) > 0 and j >= 0:
                if dp[j] is True:
                    if s[j+1:i+1] in wordDict:
                        found = True
                        break
                j -= 1
                
            if s[j+1:i+1] in wordDict:
                found = True
            
            dp.append(found)

        return dp[-1]