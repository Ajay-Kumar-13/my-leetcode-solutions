class Solution:
    def numDecodings(self, s: str) -> int:

        alphaindex = {
            '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', 
            '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', 
            '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', 
            '26': 'z'
        }

        if s[0] == '0':
            return 0

        dp = []

        for i in range(len(s)):

            if i == 0:
                dp.append(1)
            elif i == 1:
                n = s[i]
                ind = s[i-1]+s[i]
                if n in alphaindex and ind in alphaindex:
                    dp.append(2)
                elif n not in alphaindex and ind not in alphaindex:
                    return 0
                else:
                    dp.append(1)
            else:
                n = s[i]
                ind = s[i-1]+s[i]

                if n not in alphaindex and ind not in alphaindex:
                    return 0
                elif n == "0" and ind in alphaindex:
                    dp.append(dp[i-2])
                elif n in alphaindex and ind in alphaindex:
                    dp.append(dp[i-1]+dp[i-2])
                else:
                    dp.append(dp[i-1])
                

        return dp[-1]