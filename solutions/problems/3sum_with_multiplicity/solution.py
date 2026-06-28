class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        
        def possibleCombinations(n, r):
            if n < r:
                return 0
                
            numerator = 1
            denominator = 1
            
            for i in range(r):
                numerator = numerator * (n-i)
                denominator = denominator * (i+1)
                
            return numerator // denominator
        
        count = 0
        
        frequency = {}

        for ele in arr:
            frequency[ele] = frequency.get(ele, 0)+1
            
        
        arr = sorted(list(set(arr)))
        
        for i in range(len(arr)):
            k = len(arr) - 1
            j = i
            while j <= k:
                
                t = target - arr[j] - arr[k]

                if t == arr[i]:
                    
                    if arr[i] == arr[j] and arr[j] == arr[k]:
                        count += possibleCombinations(frequency.get(arr[j]), 3)
                    elif arr[j] == arr[k]:
                        count += possibleCombinations(frequency.get(arr[j]), 2) * frequency.get(arr[i])
                    elif arr[i] == arr[j]:
                        count += frequency.get(arr[k]) * possibleCombinations(frequency.get(arr[i]), 2)
                    else:
                        count += frequency.get(arr[i]) * frequency.get(arr[j]) * frequency.get(arr[k])                    
                    
                    j += 1
                    k -= 1
                elif t < arr[i]:
                    k -= 1
                else:
                    j += 1
                    

        return count % 1000000007