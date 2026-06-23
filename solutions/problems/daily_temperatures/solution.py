class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0]
        coolTemp = [0]
        
        for i in range(1, len(temperatures)):
            ans.append(0)
            if temperatures[i] < temperatures[coolTemp[-1]]:
                coolTemp.append(i)
            else:
                while len(coolTemp) > 0 and temperatures[i] > temperatures[coolTemp[-1]]:
                    ans[coolTemp[-1]] = i - coolTemp[-1]
                    coolTemp.pop()
                coolTemp.append(i)

        return ans