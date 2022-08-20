import heapq
from turtle import position


def minRefuelStops(target, startFuel, stations) -> int:
        
        stations.append([target, 0])    
        fuel = startFuel
        refuelingCount, previousStation = 0, 0
        missedStation = []
        
        for position, gas in stations:
            distance, previousStation = position - previousStation, position    
            
            if fuel < distance:  
                
                while missedStation and fuel < distance: 
                    fuel += heapq.heappop(missedStation)
                    refuelingCount += 1   
                    
                if fuel < distance: return -1   
                
            fuel -= distance
            heapq.heappush(missedStation, gas)  
            
        return refuelingCount



target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
result = minRefuelStops(target,startFuel,stations)
print('minimum refills required is:',result)
