class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            breadth = j - i
            length = min(height[i], height[j])
            max_area = max(max_area, (length * breadth))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area