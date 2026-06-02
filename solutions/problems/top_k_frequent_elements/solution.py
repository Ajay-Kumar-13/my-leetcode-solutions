class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}

        for num in nums:
            if num not in frequency:
                c = nums.count(num)
                frequency[num] = c

        values = list(set(frequency.values()))
        values.sort()
        values.reverse()

        final_list = []

        for i in range(k):
            val = values[i]
            for key, v in frequency.items():
                if v == val and len(final_list) < k:
                    final_list.append(key)
            if (len(final_list) >= k):
                break
        return final_list