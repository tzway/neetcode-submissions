from collections import namedtuple
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time to destination if no obstacle
        def get_min_time(car):
            return (target - car.p) / car.s

        Car = namedtuple("Car", "p s")
        cars = [Car(position[i],speed[i]) for i in range(len(position))]
        
        fleetCount = 1
        stack = [] # Mono Descend
        for car in sorted(cars, key=lambda car: car.p, reverse=True):
            if stack and get_min_time(car) > stack[0]:
                stack = []
                fleetCount += 1
            stack.append(get_min_time(car))
        return fleetCount
