from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int) # num:int -> count:int

        for n in nums:
            countMap[n] += 1
        
        bucket = defaultdict(list) # count:int -> nums of count freq:list

        for num, count in countMap.items():
            bucket[count].append(num)
        
        res = []
        for count in range(len(nums), 0, -1):
            res.extend(bucket[count])
            k -= len(bucket[count])
            if k == 0:
                return res