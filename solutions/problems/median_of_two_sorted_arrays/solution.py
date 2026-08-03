class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1,n2 = n2, n1

        i = 0
        j = min(n1, n2)

        totalElementsInLeft = (n1+n2+1)//2

        while i <= j:
            mid1 = (i+j)//2
            mid2 = totalElementsInLeft - mid1

            l1 = -float('inf')
            l2 = -float('inf')
            r1 = float('inf')
            r2 = float('inf')

            if mid1-1 >= 0:
                l1 = nums1[mid1-1]
            
            if mid2-1 >= 0:
                l2 = nums2[mid2-1]

            if mid1 < n1:
                r1 = nums1[mid1]

            if mid2 < n2:
                r2 = nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                if (n1+n2) % 2 == 0:
                    return (max(l1,l2)+min(r1,r2)) / 2.0
                else:
                    return max(l1, l2)

            elif l2 > r1:
                i = mid1 + 1
            else:
                j = mid1 - 1
        
        return 0