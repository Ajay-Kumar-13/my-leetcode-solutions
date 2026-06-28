class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        prefixMax = []
        suffixMax = []

        maxPrefix = 0
        maxSuffix = 0

        for h in height:
            maxPrefix = max(maxPrefix, h)
            prefixMax.append(maxPrefix)

        for i in range(len(height)-1, -1, -1):
            maxSuffix = max(maxSuffix, height[i])
            suffixMax.append(maxSuffix)

        suffixMax.reverse()

        maxTrappedUnits = 0

        for i,h in enumerate(height):
            units = min(prefixMax[i], suffixMax[i]) - h
            if units > 0:
                maxTrappedUnits += units

        return maxTrappedUnits