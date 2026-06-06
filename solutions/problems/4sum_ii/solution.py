class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """

        first_array = []
        second_array = []
        count = 0
        mappings = {}

        for i,n1 in enumerate(nums1):
            for j,n2 in enumerate(nums2):
                sum1 = n1 + n2
                sum2 = nums3[i] + nums4[j]
                first_array.append(sum1)
                second_array.append(sum2)

        for s in first_array:
            negative = 0 - s
            if s not in mappings:
                c = second_array.count(negative)
                count += c
                mappings[s] = c
            else:
                count += mappings.get(s)

        return count