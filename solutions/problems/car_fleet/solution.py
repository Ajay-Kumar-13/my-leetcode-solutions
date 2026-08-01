class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        n = len(position)

        cars_stats = {}

        for i in range(n):
            cars_stats[position[i]] = speed[i]

        position.sort()

        for i in range(n):
            fleet = 0
            t = (target-position[i])/cars_stats.get(position[i])

            while len(stack) > 0 and stack[-1] <= t:
                stack.pop()
            
            stack.append(t)

        return len(stack)