class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        LM = 0
        RM = 0
        PrefixMaxArray = []
        SuffixMaxArray = []

        for element in height:
            LM = max(LM, element)
            PrefixMaxArray.append(LM)

        for i in range(len(height) - 1, -1, -1):
            RM = max(RM, height[i])
            SuffixMaxArray.append(RM)

        SuffixMaxArray.reverse()


        total = 0

        for i in range(len(height)):
            LeftMax = PrefixMaxArray[i]
            RightMax = SuffixMaxArray[i]

            total += (min(LeftMax, RightMax) - height[i])

        return total

