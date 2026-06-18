class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        frequency = {}

        i = 0 
        j = 0

        maxLength = 0

        while j < len(fruits):

            frequency[fruits[j]] = frequency.get(fruits[j], 0)+1

            if len(frequency) >= 3:
                maxLength = max(maxLength, j-i)
                while i < j and len(frequency) >= 3:
                    frequency[fruits[i]] = frequency.get(fruits[i]) - 1
                    if frequency.get(fruits[i]) == 0:
                        frequency.pop(fruits[i]) 
                    i += 1
                    break
            j += 1
        
        maxLength = max(maxLength, j-i)

        return maxLength
        