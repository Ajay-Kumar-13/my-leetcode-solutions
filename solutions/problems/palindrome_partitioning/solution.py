class Solution:
    def partition(self, string: str) -> List[List[str]]:
        l = len(string)
        dp = [[False]*l for _ in range(l)]

        palindromes = []
        current = []

        for j in range(l):
            for i in range(0, j+1):
                if i == j:
                    dp[i][j] = True
                    continue
                
                if string[i] == string[j] and j-i == 1:
                    dp[i][j] = True
                elif string[i] == string[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    
        def checkPalindromes(start_index):
            if start_index == l:
                palindromes.append(current[:])
                return 
            
            for end in range(start_index, l):
                if dp[start_index][end]:
                    current.append(string[start_index:end+1])
                    checkPalindromes(end+1)
                    current.pop()

        checkPalindromes(0)

        return palindromes
