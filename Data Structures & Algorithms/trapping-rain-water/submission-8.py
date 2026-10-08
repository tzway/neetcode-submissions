class Solution:
    def trap(self, height: List[int]) -> int:
        def find_highest(start, stop):
            highest_p = start
            for i in range(start, stop):
                if height[highest_p] < height[i]:
                    highest_p = i
                    
            return highest_p

        walls = []

        highest_p = find_highest(0, len(height))
        walls.append(highest_p)
        # print(walls)

        r_border = highest_p
        l_border = highest_p +1

        while r_border> 0:
            hp = find_highest(0, r_border-1)
            walls.append(hp)
            r_border = hp
            # print(walls)

        while l_border< len(height):
            hp = find_highest(l_border+1, len(height))
            if hp< len(height):
                walls.append(hp)
            l_border = hp
            # print(walls)
        
        walls.sort()
            


        

        
        
        def get_water_between(left, right):
            level = min(height[left], height[right])
            print(f'water level {level}')
            water = 0
            for i in range(left+1, right):
                water += level - min(level,height[i])
            print(f'water amount {water}')
            return water
        
        all_water = 0
        for i in range(len(walls)-1):
            print(f"iterate {i}")
            all_water += get_water_between(walls[i],walls[i+1])

        return all_water
