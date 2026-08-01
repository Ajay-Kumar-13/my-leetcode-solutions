class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l = len(s)
    
        dp = [[False] * len(s) for _ in range(l)]
        
        palindrome = ""
        
        for i in range(l-1,-1,-1):
            
            for j in range(i, l):
                
                if i == j:
                    dp[i][j] = True
                    if j-i+1 > len(palindrome):
                        palindrome = s[i:j+1]
                elif i == j-1 and s[i] == s[j]:
                    dp[i][j] = True
                    if j-i+1 > len(palindrome):
                        palindrome = s[i:j+1]
                else:
                    if s[i] == s[j] and dp[i+1][j-1] is True:
                        dp[i][j] = True
                        if j-i+1 > len(palindrome):
                            palindrome = s[i:j+1]
                
        return palindrome