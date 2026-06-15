class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        suffixProd = 1
        prefixProd = 1

        suffixProducts = {}
        prefixProducts = {}

        answer = []

        for i in range(len(nums)):
            prefixProd *= nums[i]
            prefixProducts[i] = prefixProd

        for i in range(len(nums)-1, -1, -1):
            suffixProd *= nums[i]
            suffixProducts[i] = suffixProd

        for i in range(len(nums)):
            prod = prefixProducts.get(i-1, 1) * suffixProducts.get(i+1, 1)
            answer.append(prod)

        return answer