class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x:x[0])
        stack = [points[0]]

        def inCurrentInterval(existingInterval, newInterval):
            return existingInterval[1] >= newInterval[0]

        for i in range(1, len(points)):
            point = points[i]
            if not inCurrentInterval(stack[-1], point):
                stack.append(point)
            else:
                stack[-1] = [max(stack[-1][0], point[0]), min(stack[-1][1], point[1])]

        return len(stack)