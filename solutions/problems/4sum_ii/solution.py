class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        
        leftArray = {}

        answer = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                leftArray[nums1[i] + nums2[j]] = leftArray.get(nums1[i] + nums2[j], 0)+1

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                s = nums3[i] + nums4[j]
                if 0-s in leftArray:
                    val = leftArray.get(0-s)
                    answer += val
        return answer