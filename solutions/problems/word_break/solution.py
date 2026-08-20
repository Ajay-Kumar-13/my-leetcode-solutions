class Solution:
    def wordBreak(self, s, wordDict):
        
        words = {}
        
        def validateDict(s):

            if s in words:
                return words[s]

            if not s:
                return True

            word = ""
            for i in range(len(s)):
                word += s[i]
                if word in wordDict:
                    if validateDict(s[i+1:]):
                        words[s[:i]] = True
                        return True

            words[s] = False
            return False

        return validateDict(s)