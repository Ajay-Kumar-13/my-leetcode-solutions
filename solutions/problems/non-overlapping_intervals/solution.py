class Solution:
    def quickSort(self, intervals):
    
        if not intervals:
            return []
        
        if len(intervals) <= 1:
            return intervals
            
        pivot = intervals[-1][:]
        
        L, R= [], []
        
        for i in range(len(intervals)-1):
            interval = intervals[i]
            if pivot[1] <= interval[1]:
                R.append(interval[:])
            else:
                L.append(interval[:])
                
        L = self.quickSort(L)
        R = self.quickSort(R)
        
        return L+[pivot]+R
        
    def notInCurrentInterval(self, existingInterval, newInterval):
        return existingInterval[1] <= newInterval[0]
        
    def eraseOverlapIntervals(self, intervals):

        # intervals = self.quickSort(intervals)
        intervals.sort(key=lambda x: x[1])
        stack = [intervals[0][:]]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if self.notInCurrentInterval(stack[-1], interval):
                stack.append(interval[:])
            
        return len(intervals) - len(stack)