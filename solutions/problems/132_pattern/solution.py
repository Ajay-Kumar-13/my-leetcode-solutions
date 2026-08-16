class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []
        n = len(nums)
        two = -float('inf')
        for i in range(n-1, -1, -1):

            if nums[i] < two:
                return True
            
            while len(stack) > 0 and stack[-1] < nums[i]:
                two = max(two, stack.pop())

            stack.append(nums[i])

        return False