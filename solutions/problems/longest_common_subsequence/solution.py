class Solution:

    def getLongestLength(self, ind1, ind2, text1, text2, dp):

        if ind1 == len(text1) or ind2 == len(text2):
            return 0
        elif dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        
        if text1[ind1] == text2[ind2]:
            dp[ind1][ind2] = 1 + self.getLongestLength(ind1+1, ind2+1, text1, text2, dp)
            return dp[ind1][ind2]
        else:
            dp[ind1][ind2] =  max(self.getLongestLength(ind1+1, ind2, text1, text2, dp), self.getLongestLength(ind1, ind2+1, text1, text2, dp))
            return dp[ind1][ind2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[-1]*len(text2) for _ in range(len(text1))]
        
        return self.getLongestLength(0, 0, text1, text2, dp)