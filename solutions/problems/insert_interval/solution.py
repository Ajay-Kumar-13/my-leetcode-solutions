class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = [newInterval]
        foundInterval = False

        def inCurrentInterval(existing, new):
            return existing[0] <= new[0] and existing[1] >= new[1]
        
        for interval in intervals:
            if not inCurrentInterval(stack[-1], interval):
                if interval[0] < stack[-1][0] and interval[1] < stack[-1][0]:
                    prev = stack.pop()
                    stack.append(interval[:])
                    stack.append(prev[:])
                elif interval[0] > stack[-1][1] and interval[0] > stack[-1][1]:
                    stack.append(interval[:])
                else:
                    stack[-1] = [min(stack[-1][0], interval[0]), max(stack[-1][1], interval[1])]

        return stack