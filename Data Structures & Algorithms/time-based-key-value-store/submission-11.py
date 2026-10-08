from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = {}
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[(key,timestamp)] = value
        self.timemap[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ''
        if (key, timestamp) in self.hashmap:
            return self.hashmap[(key,timestamp)]
        
        timeSerial = self.timemap[key]
        left, right = 0, len(timeSerial) -1
        while left <= right:
            middle = (left+right)//2
            print(left)
            print(right)
            middleVal = timeSerial[middle]

            if middleVal < timestamp:
                
                left = middle + 1
                
            if middleVal > timestamp:
                right = middle -1
        if timeSerial[right] < timestamp:
            return self.hashmap[key,timeSerial[right]]
        return ''
