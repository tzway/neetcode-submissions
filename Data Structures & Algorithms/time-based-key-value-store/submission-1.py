class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[(key,timestamp)] = value
        

    def get(self, key: str, timestamp: int) -> str:
        for t in range(timestamp,0, -1):
            if (key,t) in self.hashmap:
                return self.hashmap[(key,t)]
        return ""
