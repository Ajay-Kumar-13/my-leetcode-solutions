class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        first_array = []
        second_array = []

        for num in nums1:
            if num not in nums2:
                first_array.append(num)

        for num in nums2:
            if num not in nums1:
                second_array.append(num)

        return [list(set(first_array)), list(set(second_array))]    