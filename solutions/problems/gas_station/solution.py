class Solution:
    def canCompleteCircuit(self, gas, cost):
        
        l = len(gas)
        i = 0
        while i < l*2:
            a = i % l
    
            remainingGas = 0
            
            if gas[a] + remainingGas >= cost[a]:
                
                remainingGas = gas[a] - cost[a]
                
                for j in range(i+1, l*2):
                    b = j % l
                    
                    if a == b:
                        return a
                    currentGas = gas[b] + remainingGas   
                    if currentGas < cost[b]:
                        if b < i:
                            return -1
                        i = b
                        remainingGas = 0
                        break
                    else:
                        remainingGas = currentGas - cost[b]
            i += 1
        
        return -1