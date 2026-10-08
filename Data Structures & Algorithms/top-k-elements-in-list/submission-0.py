class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcount = defaultdict(int) # element: count
        for n in nums:
            numcount[n] +=1
        sortedarr = [item[0] for item in sorted(numcount.items(), key= lambda item: item[1] )]
        return sortedarr[-k:]