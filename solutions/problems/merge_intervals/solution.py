class Solution:
    
    def quickSort(self, intervals):
        if not intervals:
            return []
        if len(intervals) <= 1:
            return intervals
            
        pivot = intervals[-1]
        
        L, R = [], []
        
        for i in range(len(intervals)-1):
            interval = intervals[i]
            if interval[0] <= pivot[0]:
                L.append(interval[:])
            else:
                R.append(interval[:])
                
        L = self.quickSort(L)
        R = self.quickSort(R)
        
        return L + [pivot[:]] + R
        
    def notInCurrentInterval(self, existingInterval, newInterval):
        return existingInterval[1] < newInterval[0] and existingInterval[1] < newInterval[1]
    
    def merge(self, intervals):
        intervals = self.quickSort(intervals)
        
        stack = [intervals[0]]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if self.notInCurrentInterval(stack[-1], interval):
                stack.append(interval)
            else:
                stack[-1] = [min(stack[-1][0], interval[0]), max(stack[-1][1], interval[1])]
        
        return stack