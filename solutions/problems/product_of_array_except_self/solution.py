class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        postfix = []
        output = []

        pre_product = 1
        post_product = 1

        for i in range(len(nums)):
            product = nums[i] * pre_product
            pre_product = product
            prefix.append(product)

        for i in range(len(nums) - 1, -1, -1):
            product = nums[i] * post_product
            post_product = product
            postfix.append(product)

        postfix.reverse()
        
        output.append(postfix[1])

        for i in range(1, len(nums)-1):
            product = postfix[i+1] * prefix[i-1]
            output.append(product)

        output.append(prefix[len(nums) - 2])

        return output
        