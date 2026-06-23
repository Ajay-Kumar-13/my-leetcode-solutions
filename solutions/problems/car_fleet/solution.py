class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
                # if there is only a single position
        if len(position) < 2:
            return 1
            
        # Map cars with their speeds
        carSpeed = {}
        for i,x in enumerate(position):
            carSpeed[x] = speed[i]
        
        # sort the array 
        position.sort()
        
        
        n = len(position)
        
        timeTakenByTheCar = []
        
        for i in range(n):
            time = (target-position[i]) / carSpeed.get(position[i])
            
            while len(timeTakenByTheCar) > 0 and time >= timeTakenByTheCar[-1]:
                timeTakenByTheCar.pop()
                    
            timeTakenByTheCar.append(time)
            
        return len(timeTakenByTheCar)