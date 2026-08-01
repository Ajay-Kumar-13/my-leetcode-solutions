class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        lt1 = len(text1)+1
        lt2 = len(text2)+1

        dp = [[0] * (lt2) for _ in range(lt1)]
        
        
        for i in range(1, lt1):
            for j in range(1, lt2):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[lt1-1][lt2-1]