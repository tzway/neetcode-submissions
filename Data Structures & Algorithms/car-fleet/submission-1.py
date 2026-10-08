
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def time(car):
            p, v = car
            return (target - p) / v
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack = []
        for car in cars:
            if not stack or stack[-1] < time(car):
                stack.append(time(car))
                continue
            
            if stack[-1] >= time(car):
                continue

        
        return len(stack)