class Solution:

    def minOperations(self, ind1, ind2, word1, word2, dp):
        
        # Insertion
        if ind1 == len(word1) and ind2 < len(word2):
            val = len(word2) - ind2
            # dp[ind1][ind2] = val
            return val
        elif ind1 == len(word1):
            # dp[ind1][ind2] = 0
            return 0

        # Deletion
        if ind2 == len(word2) and ind1 < len(word1):
            val = len(word1) - ind1
            # dp[ind1][ind2] = val
            return val
        elif ind2 == len(word2):
            # dp[ind1][ind2] = 0
            return 0

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        if word1[ind1] != word2[ind2]:
            # min(replace, delete, insert)
            val = min(
                    1+self.minOperations(ind1+1, ind2+1, word1, word2, dp), 
                    1+self.minOperations(ind1+1, ind2, word1, word2, dp),
                    1+self.minOperations(ind1, ind2+1, word1, word2, dp)
                )
            dp[ind1][ind2] = val
            return val
        else:
            val = self.minOperations(ind1+1, ind2+1, word1, word2, dp)
            dp[ind1][ind2] = val
            return val

    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[-1]*len(word2) for _ in range(len(word1))]
        
        return self.minOperations(0, 0, word1, word2, dp)